import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# -------------------------------
# CRISP-DM Step 1: Business Understanding
# -------------------------------
st.title("Simple Linear Regression Demo — CRISP-DM 流程")
st.markdown("""
**目標**：透過簡單線性回歸 (y = a·x + b + noise)，了解資料間的線性關係與模型效能。  
**流程**：CRISP-DM → 商業理解 → 資料理解 → 資料準備 → 建模 → 評估 → 部署。
""")

# -------------------------------
# Step 2 + 3: Data Understanding / Preparation
# -------------------------------
st.sidebar.header("Data Generation")
a = st.sidebar.slider("Slope (a)", -5.0, 5.0, 2.0, step=0.1)
b = st.sidebar.slider("Intercept (b)", -10.0, 10.0, 1.0, step=0.5)
noise = st.sidebar.slider("Noise level", 0.0, 10.0, 1.0, step=0.1)
n = st.sidebar.slider("Number of points", 10, 500, 100, step=10)
seed = st.sidebar.number_input("Random seed", 0, 9999, 42)

np.random.seed(seed)
x = np.linspace(0, 10, n)
y = a * x + b + np.random.normal(0, noise, n)

df = pd.DataFrame({"x": x, "y": y})
st.subheader("Data Preview")
st.dataframe(df.head())

# -------------------------------
# Step 4: Modeling
# -------------------------------
X = df[["x"]]
y = df["y"]
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# -------------------------------
# Step 5: Evaluation
# -------------------------------
r2 = r2_score(y, y_pred)
mse = mean_squared_error(y, y_pred)

st.subheader("Model Evaluation")
st.write(f"**Estimated Model:** y = {model.coef_[0]:.3f}·x + {model.intercept_:.3f}")
st.write(f"R² = {r2:.3f}, MSE = {mse:.3f}")

fig, ax = plt.subplots()
ax.scatter(x, y, label="Data", alpha=0.7)
ax.plot(x, y_pred, color="red", label="Regression Line")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
st.pyplot(fig)

# -------------------------------
# Step 6: Deployment
# -------------------------------
st.markdown("""
### 🚀 部署教學
1. 將此檔案命名為 **app.py**  
2. 上傳至 GitHub  
3. 建立 `requirements.txt` 檔案（如下）  
4. 前往 [Streamlit Cloud](https://share.streamlit.io/) → 連接 GitHub Repo → 按「Deploy」  
5. 網頁即會自動部署完成！
""")
