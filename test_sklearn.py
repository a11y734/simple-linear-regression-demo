from sklearn.linear_model import LinearRegression
import numpy as np

# 範例資料
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# 建立模型
model = LinearRegression()
model.fit(X, y)

# 預測
print(model.predict(np.array([[6]])))
