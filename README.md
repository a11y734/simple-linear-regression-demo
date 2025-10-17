📉 Simple Linear Regression Demo — CRISP-DM 流程

這是一個使用 **Streamlit** 建立的互動式簡單線性回歸範例應用。
它嚴格遵循 **CRISP-DM** (Cross-Industry Standard Process for Data Mining) 的完整流程，並允許使用者修改模型參數以即時觀察變化。

## ✨ 核心功能 (Features)

這個演示應用程式涵蓋了資料科學專案的完整生命週期：

### CRISP-DM 六階段演示

* 遵循 CRISP-DM 六階段：

  1. 商業理解 (Business Understanding)

  2. 資料理解 (Data Understanding)

  3. 資料準備 (Data Preparation)

  4. 建模 (Modeling)

  5. 評估 (Evaluation)

  6. 部署 (Deployment)

### 互動式參數調整

使用者可以在應用程式的側邊欄即時調整以下數據生成參數：

* **斜率 a**: 影響 $Y = ax + b$ 中的數據趨勢。

* **截距 b**: 影響 $Y = ax + b$ 中的數據起點。

* **噪音大小**: 控制數據點相對於回歸線的分散程度。

* **資料點數 n**: 決定用於訓練的數據量。

### 模型輸出與評估

* 使用 `scikit-learn` 訓練線性回歸模型。

* 即時顯示：回歸線、模型方程式、R² (決定係數)、MSE (均方誤差) 等關鍵指標。

## 💻 本地執行方式 (Local Execution)

要運行此應用程式，您需要安裝 Python 環境及相關套件。

### 步驟 1: 安裝依賴套件

請確保您的環境中已安裝 Streamlit、Numpy、Pandas 和 Scikit-learn。

```
pip install -r requirements.txt





```

### 步驟 2: 啟動應用程式

在專案目錄下執行以下指令：

```
streamlit run app.py





```

## 🌐 線上 Demo (Live Deployment)

您可以直接點擊以下連結，無需本地安裝即可體驗應用程式：

[🌐 **Streamlit 線上 Demo 連結**](https://simple-linear-regression-demo-jpxqwh6gi65xzymh5ucuan.streamlit.app/)

## 🚀 Promote

write python to solve simple linear regression problem,
1.CRISP-DM
2.allow user to modify a in ax+b, noise, number of points
3.streamlit or flask web, 框架 deployment
giveme complete code,列出所需要安裝的套件及流程