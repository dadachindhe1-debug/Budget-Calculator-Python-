import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# AI Machine Learning Expense Predictor (Linear Regression)
# Past 5 months training data
months = np.array([,,,,])
expenses = np.array()

# Create and train the Machine Learning model
model = LinearRegression()
model.fit(months, expenses)

# Predict expense for a user-specified future month
target_month = int(input("Enter the future month number to predict (e.g., 6, 12, 24): "))
prediction = model.predict([[target_month]])

print("---------------------------------")
print(f"AI Prediction for Month {target_month}: {round(prediction, 2)} Rs")

# Visualize past data and future AI prediction
plt.scatter(months, expenses, color='blue', label='Past Expenses (Actual)')
plt.scatter([target_month], prediction, color='red', s=100, label=f'AI Prediction (Month {target_month})')
plt.plot(np.append(months, target_month), model.predict(np.append(months, [[target_month]], axis=0)), color='green', linestyle='--', label='AI Trend Line')

plt.title("AI Expense Forecast Model")
plt.xlabel("Month Number")
plt.ylabel("Expense (in Rs)")
plt.legend()
plt.grid(True)
plt.show()
