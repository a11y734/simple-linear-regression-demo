import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import plotly.express as px
import plotly.graph_objects as go

# --- CRISP-DM Phase 1: 商業理解 (Business Understanding) ---
st.set_page_config(layout="wide")
st.title("使用 Streamlit 進行簡單線性迴歸分析 (CRISP-DM 框架)")

st.header("1. 商業理解 (Business Understanding)")
st.write(
    "我們的商業目標是理解和模擬兩個變數之間的線性關係。在這個互動式應用中，我們將探索如何透過調整線性方程式的參數、"
    "資料點的數量以及雜訊程度，來觀察線性迴歸模型的表現。這有助於我們理解模型的敏感度和準確性。"
)
st.write("線性方程式為: **y = a * x + b + noise**")

# --- 使用者輸入介面 ---
st.sidebar.header("參數調整")
st.sidebar.write("透過調整以下參數來生成新的資料集並訓練模型。")

# 允許使用者修改 a, noise, 和 number of points
a_slope = st.sidebar.slider("斜率 (a)", min_value=-10.0, max_value=10.0, value=2.5, step=0.1)
b_intercept = 50.0  # 固定截距 b
noise_level = st.sidebar.slider("雜訊強度", min_value=0.0, max_value=50.0, value=10.0, step=1.0)
num_points = st.sidebar.slider("資料點數量", min_value=10, max_value=1000, value=100, step=10)

# --- CRISP-DM Phase 2 & 3: 資料理解與準備 (Data Understanding & Preparation) ---
st.header("2. 資料理解與準備 (Data Understanding & Data Preparation)")

@st.cache_data
def generate_data(a, b, noise, n_points):
    """根據使用者輸入的參數生成資料"""
    x = np.linspace(0, 100, n_points)
    noise_array = np.random.normal(0, noise, n_points)
    y = a * x + b + noise_array
    df = pd.DataFrame({'X': x, 'y': y})
    return df

data = generate_data(a_slope, b_intercept, noise_level, num_points)

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("資料預覽")
    st.write("這是根據您設定的參數所生成的資料集。")
    st.dataframe(data.head())
    st.write(f"總共生成了 **{len(data)}** 筆資料。")

with col2:
    st.subheader("資料視覺化")
    st.write("下圖顯示了生成的資料點分佈情況。")
    fig_scatter = px.scatter(data, x='X', y='y', title="生成的資料分佈圖")
    st.plotly_chart(fig_scatter, use_container_width=True)

# 資料準備說明
st.write(
    "**資料準備說明**：在此階段，我們將生成的資料分為特徵 (X，自變數) 和目標 (y，應變數)。"
    "由於資料是模擬生成的，因此不需要進行複雜的清理或轉換。"
)
X = data[['X']]
y = data['y']

# --- CRISP-DM Phase 4: 模型建立 (Modeling) ---
st.header("4. 模型建立 (Modeling)")
st.write(
    "我們將使用 Scikit-learn 函式庫中的 `LinearRegression` 模型來擬合數據。"
    "此模型會找出最適合資料點的直線，也就是迴歸線。"
)

# 建立並訓練模型
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# 取得模型參數
model_slope = model.coef_[0]
model_intercept = model.intercept_

st.subheader("模型結果")
st.write(f"模型找出的斜率 (a): **{model_slope:.4f}** (您設定的斜率為: {a_slope})")
st.write(f"模型找出的截距 (b): **{model_intercept:.4f}** (固定的截距為: {b_intercept})")


# --- CRISP-DM Phase 5: 模型評估 (Evaluation) ---
st.header("5. 模型評估 (Evaluation)")
st.write(
    "在此階段，我們評估模型的表現。常用的評估指標包括均方誤差 (MSE) 和 R 平方值 (R²)。"
    "我們也會將迴歸線與原始資料點一起繪製出來，以直觀地評估擬合效果。"
)

# 計算評估指標
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

col3, col4 = st.columns(2)
with col3:
    st.metric(label="均方誤差 (Mean Squared Error)", value=f"{mse:.2f}")
    st.write("MSE 越小，表示模型的預測值與實際值的差距越小。")

with col4:
    st.metric(label="R 平方值 (R-squared)", value=f"{r2:.4f}")
    st.write("R² 範圍在 0 到 1 之間，越接近 1 表示模型對資料的解釋能力越強。")

st.subheader("迴歸線視覺化")
fig_regression = go.Figure()
# 原始資料點
fig_regression.add_trace(go.Scatter(x=data['X'], y=data['y'], mode='markers', name='原始資料'))
# 迴歸線
fig_regression.add_trace(go.Scatter(x=data['X'], y=y_pred, mode='lines', name='迴歸線 (模型預測)', line=dict(color='red', width=3)))

fig_regression.update_layout(title="線性迴歸擬合結果", xaxis_title="X (自變數)", yaxis_title="y (應變數)")
st.plotly_chart(fig_regression, use_container_width=True)


# --- CRISP-DM Phase 6: 部署 (Deployment) ---
st.header("6. 部署 (Deployment)")
st.write(
    "這個 Streamlit 應用程式本身就是一個部署的範例。它將整個資料科學流程（從資料生成到模型評估）"
    "打包成一個互動式的 Web 應用，讓非技術背景的使用者也能輕易地操作和理解線性迴歸模型。"
)
st.info(
    "**如何與此應用互動？**\n"
    "1.  **調整左側邊欄的參數**：嘗試不同的斜率、雜訊強度和資料點數量。\n"
    "2.  **觀察變化**：查看資料分佈圖、模型評估指標和迴歸線如何隨著您的調整而改變。\n"
    "3.  **獲得洞察**：例如，您可以觀察到當雜訊增加時，R² 值會下降，表示模型的解釋能力變差。"
)