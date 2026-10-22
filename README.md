# 🎮 遊戲數據分析作品集 (Game Data Analysis Portfolio)

本倉庫包含兩個獨立的數據分析專案，展示如何以 **Python (Pandas) 進行資料清理與特徵工程**，並運用 **類似 SQL 的多表核對邏輯**，將原始數據整理成可供營運與行銷參考的分析結論。

---

## 📊 專案一：手遊玩家付費行為分析 (`game_analysis.ipynb`)

分析手遊玩家的付費資料，比較不同年齡層、性別、遊戲類型與首次付費時機的付費金額。

*   **資料來源：** Kaggle 公開資料集 Mobile Game In-App Purchases Dataset 2025，共 3,024 筆玩家資料。
*   **使用工具：** Python（Pandas、Matplotlib）、Tableau Public。
*   **分析流程：**
    *   **資料前處理：** 使用 Pandas 檢查資料結構、重複值與缺值。
    *   **特徵工程：** 運用 `pd.cut` 將連續型變數（年齡、首次付費天數）分組。
    *   **統計分析：** 透過 `groupby`、`mean` 等聚合函數進行多維度交叉比較，並以 Matplotlib 繪製圖表。
    *   **儀表板：** 以 Tableau Public 呈現平均付費、中位數付費與高額付費玩家（Whale）占比。
*   **主要發現（平均付費）：**
    1.  35-50 歲玩家平均付費最高（$124），約為 18-25 歲（$60）的 2.1 倍；男性平均付費（$115）高於女性（$87）。
    2.  安裝後 8-15 天首次付費者的平均消費最高（$123）。
    3.  Racing（$160）與 Battle Royale（$157）平均付費最高，Action RPG（$63）與 Sandbox（$68）最低。
*   **限制與補充：**
    *   各年齡層、性別、首次付費天數與遊戲類型的**中位數付費都落在約 11-13 美元**，差異很小。
    *   平均付費的差異主要來自少數高額付費玩家。Whale 占比在 18-25 歲約 1.4%、35-50 歲約 2.6%，人數不多。
    *   以上結論僅限於此資料集，未進行統計檢定，不宜直接推論到其他遊戲或市場。
*   **互動式儀表板：** [Tableau Public](https://public.tableau.com/app/profile/j.y2367/viz/Game_analysis_17925714893860/sheet3)

<!-- 上傳儀表板截圖到 images/dashboard.png 後，把下面這行的註解拿掉
![Tableau 儀表板截圖](images/dashboard.png)
-->

---

## 📈 專案二：遊戲平台廣告版位效益分析 (`platform_ad_analysis.ipynb`)

聚焦於跨管道流量與廣告版位成效，比較各廣告來源的點擊轉換率與投資報酬率（ROI）。

*   **核心技術：**
    *   運用類似 SQL `JOIN` 的邏輯進行多表欄位串聯與交叉比對。
    *   檢查每日流量指標，排查異常點擊與低效版位。
*   **主要發現：**
    *   找出曝光量高但轉換率（CVR）偏低的版位，並據此提出重新分配廠商預算的建議。

---

## 🛠️ 技能與工具 (Skills & Tools)

*   **資料庫查詢 (SQL)：** 多表合併（`JOIN`/`ON`）、分組統計（`GROUP BY`）與常用聚合函數（`SUM`、`AVG`、`COUNT`），可進行資料核對與稽核。
*   **資料分析 (Python)：** 使用 **Pandas** 進行資料清洗、缺失值處理與特徵提取，並以 **Matplotlib** 繪製圖表。
*   **視覺化 (Tableau)：** 使用 Tableau Public 建置儀表板，呈現平均、中位數與族群占比的對照。
*   **AI 輔助開發：** 使用 Generative AI（Claude、ChatGPT）輔助撰寫與優化程式，並自行核對輸出的正確性與邏輯。相關實作可參考 [lean-video-pipeline](https://github.com/YJKun-freshman/lean-video-pipeline)，其中記錄了 LLM 輸出數字錯誤的案例與對應的驗證機制。

---

📬 **聯絡方式 / Contact**

如果您對我的專案有興趣，歡迎與我聯繫。
