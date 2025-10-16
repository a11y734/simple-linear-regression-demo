# Simple Linear Regression Demo — CRISP-DM 流程

這是一個使用 **Streamlit** 建立的互動式簡單線性回歸範例應用。  
它遵循 **CRISP-DM** 的完整流程，並允許使用者修改模型參數以即時觀察變化。

---

## 🧩 功能
- 遵循 CRISP-DM 六階段（商業理解、資料理解、資料準備、建模、評估、部署）
- 可互動調整：
  - 斜率 a
  - 截距 b
  - 噪音大小
  - 資料點數 n
- 使用 sklearn 訓練線性回歸
- 即時顯示回歸線、模型方程式、R²、MSE 等指標

---

## 🚀 本地執行方式

```bash
pip install -r requirements.txt
streamlit run app.py