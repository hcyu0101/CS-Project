# CS-Project

### Week 1 (2024/07/04)
* **Paper**: Algorithmic Study on Position and Movement Method of Badminton Doubles
* **Ayalytics**: 
    * 用sklearn實作擊球區域預測
    * FCNN Classification
    * 單打

### Week 2 (2024/07/11)
* **Paper**: TacticFlow: Visual Analytics of Ever-Changing Tactics in Racket Sports
* **Ayalytics**: 
    * 用sklearn實作雙打站位跟球種的關係
    * K-means Clustering
    * 雙打

### Week 3 (2024/07/18)
* **Paper**: A Formal Methodology for Notational Analysis and Real-Time Decision Support in Sport Environment
* **Ayalytics**: 
    * 改進Week 2的內容，增加***紀錄擊球者***
    * 用sklearn實作雙打站位跟球種的關係
    * K-means Clustering，用***Elbow method***找K
    * 雙打

### Week 4 (2024/07/25)
* **Paper**: A Detailed Study of Clustering Algorithms
* **Ayalytics**: 
    * 改進Week 3的內容，增加***紀錄對手球種(one-hot-encoding)***
    * 用sklearn實作雙打站位跟球種的關係
    * 修改Dataset，挑出14號跟33號選手搭檔的shot(之前有選到14號選手跟其他人搭檔的shot)
    * K-means Clustering
    * 雙打

### Week 5 (2024/08/01)
* **Paper**: A Supervised Feature Selection Method For Mixed-Type Data using Density-based Feature Clustering
* **Ayalytics**: 
    * 延伸Week 4的內容，增加***1場比賽 v.s. 其他6場比賽***的比較
    * 用sklearn實作雙打站位跟球種的關係
    * K-means Clustering
    * 雙打

### Week 6 (2024/08/08)
* **Paper**: Clustering of mixed-type data considering concept hierarchies: problem specification and algorithm
* **Ayalytics**: 
    * 延伸Week 5的內容，檢視dataset之後發現有兩場比賽的***player AB, CD***標記錯誤，為Week 5不合理的部分做出解釋
    * 改用百分比呈現***confusion matrix***
    * 加入***得分與否***的分析
    * 用sklearn實作雙打站位跟球種的關係
    * K-means Clustering
    * 雙打

### Week 7~8 (2024/08/15、2024/08/22)
* **Paper**: Clustering of mixed-type data considering concept hierarchies: problem specification and algorithm
* **Ayalytics**: 
    * 把這兩週讀到的論文提供的開元程式碼(ClicoT)抓下來跑
    * 針對球員位置、對手擊出球種、我方回球球種進行分群，並觀察分群結果跟勝率的關係
    * 用ClicoT實作單打位置跟勝率的關係
    * ([ClicoT](https://dm.cs.univie.ac.at/research/downloads/))
    * 單打