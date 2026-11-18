import pandas as pd
import matplotlib.pyplot as plt
import os

# AI Expense Data Analyzer & Visualizer (Version 6)
filename = "my_expenses.csv"

# Auto-create sample data file if it does not exist
if not os.path.isfile(filename):
    sample_data = {
        "Category": ["Food", "Travel", "Book"],
        "Amount (Rs)": [130.0, 200.0, 50.0]
    }
    pd.DataFrame(sample_data).to_csv(filename, index=False)

# Read data using Pandas
df = pd.read_csv(filename)

print("--- Saved Data Table ---")
print(df)

# Calculate total spending per category
category_totals = df.groupby("Category")["Amount (Rs)"].sum()

print("\n--- Total Spending by Category ---")
print(category_totals)

# Plot Bar Chart using Matplotlib
category_totals.plot(kind='bar', color=['#4CAF50', '#2196F3', '#FF9800'])
plt.title("My Expense Analysis (AI Data Science Project)")
plt.xlabel("Category")
plt.ylabel("Amount (in Rs)")
plt.xticks(rotation=0)
plt.show()
