import numpy as np
import pandas as pd
from typing import List, Tuple


class PerspectiveTransform:
    def __init__(
        self,
        src: List[Tuple[float, float]],
        dst: List[Tuple[float, float]],
    ) -> None:
        self.M = self._get_perspective_projection_matrix(src, dst)

    def _get_perspective_projection_matrix(
        self,
        src: List[Tuple[float, float]],
        dst: List[Tuple[float, float]],
    ) -> np.ndarray:
        src = np.array(src, dtype=np.float32)
        dst = np.array(dst, dtype=np.float32)

        assert src.shape == dst.shape, "Source and destination shapes must match"
        assert src.shape[0] == 4, "Four source and destination points are required"

        A = np.zeros((8, 8))
        b = np.zeros((8, 1))

        for i in range(4):
            x, y = src[i]
            u, v = dst[i]
            A[i * 2] = [x, y, 1, 0, 0, 0, -u * x, -u * y]
            A[i * 2 + 1] = [0, 0, 0, x, y, 1, -v * x, -v * y]
            b[i * 2] = u
            b[i * 2 + 1] = v

        x = np.linalg.lstsq(A, b, rcond=None)[0]
        x = np.append(x, 1)
        M = x.reshape((3, 3))

        return M

    def transform(
        self,
        x: List[float],
        y: List[float],
        decimals: int = 8,
    ) -> np.ndarray:
        assert len(x) == len(y), "X and Y coordinate lists must have the same length"

        points = np.array([x, y]).T
        points = np.array(points, dtype=np.float32)
        assert points.shape[1] == 2, "Points array must have two columns for x and y"

        points_homogeneous = np.hstack((points, np.ones((len(points), 1))))
        transformed_points_homogeneous = np.dot(self.M, points_homogeneous.T)
        transformed_points = (
            transformed_points_homogeneous[:2] / transformed_points_homogeneous[2]
        ).T
        transformed_points[np.abs(transformed_points) < 10**-decimals] = 0.0
        return np.around(transformed_points, decimals)


def load_and_transform_data(
    match_file: str,
    set_file: str,
    rally_file: str,
    shot_file: str,
    output_file: str,
) -> None:
    rtns = []

    # Read CSV files
    match = pd.read_csv(match_file, low_memory=False)
    set_ = pd.read_csv(set_file, low_memory=False)
    rally = pd.read_csv(rally_file, low_memory=False)
    shot = pd.read_csv(shot_file, low_memory=False)

    # Create mapping for x and y columns
    column_mapping = {
        'player_location': ('player_location_x', 'player_location_y'),
        'opponent_location': ('opponent_location_x', 'opponent_location_y'),
        'shot_hit_position': ('shot_hit_position_x', 'shot_hit_position_y'),
        'shot_return_position': ('shot_return_position_x', 'shot_return_position_y')
    }

    for idx, row in match.iterrows():
        if row['match_id'] < 23:
            continue
        if pd.isna(row['upleft_x']):
            continue

        # Define source and target points
        src_points = [
            (row["upleft_x"], row["upleft_y"]),
            (row["upright_x"], row["upright_y"]),
            (row["downleft_x"], row["downleft_y"]),
            (row["downright_x"], row["downright_y"]),
        ]
        dst_points = [
            (0, 134),
            (61, 134),
            (0, 0),
            (61, 0),
        ]

        transformer = PerspectiveTransform(src_points, dst_points)

        # Filter data based on match_id
        set_list = set_.loc[set_["match_id"] == row["match_id"], "set_id"].tolist()
        rally_list = rally.loc[rally["set_id"].isin(set_list), "rally_id"].tolist()
        shot_list = shot.loc[shot["rally_id"].isin(rally_list), "shot_id"].tolist()
        shot_ = shot.loc[shot["shot_id"].isin(shot_list)].copy()

        # Perform coordinate transformation
        for key, (x_col, y_col) in column_mapping.items():
            if x_col in shot_.columns and y_col in shot_.columns:
                x = list(shot_[x_col])
                y = list(shot_[y_col])
                transformed = transformer.transform(x, y)
                shot_[x_col] = transformed[:, 0]
                shot_[y_col] = transformed[:, 1]
            else:
                print(f"Warning: Columns '{x_col}' or '{y_col}' not found in the dataframe")

        rtns.append(shot_)
        print(f"match_id: {row['match_id']} finished")

    # Concatenate all dataframes and save to CSV
    data = pd.concat(rtns, ignore_index=True)
    data.to_csv(output_file, index=False)


if __name__ == "__main__":
    # Replace with your actual file paths
    load_and_transform_data(
        "../dataset/Single_Badminton_0108/video_0108.csv",
        "../dataset/Single_Badminton_0108/set_0108.csv",
        "../dataset/Single_Badminton_0108/rally_0108.csv",
        "../dataset/Single_Badminton_0108/shot_0108.csv",
        "../output/Week7/convert_shot.csv"
    )
