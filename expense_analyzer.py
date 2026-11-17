# Smart Expense Tracker with Data Analysis (Bug-Free Version)

expenses = []

print("--- Welcome to AI Expense Analyzer ---")

while True:
    amount = float(input("Enter an expense amount (in Rs): "))
    expenses.append(amount)
    
    choice = input("Add another expense? (yes/no): ")
    if choice.strip().lower() != 'yes':
        break

total_expense = sum(expenses)
highest_expense = max(expenses)
average_expense = total_expense / len(expenses)

print("\n--- Your Expense Summary ---")
print("All Expenses:", expenses)
print("Total Expense:", total_expense, "Rs")
print("Highest Single Expense:", highest_expense, "Rs")
print("Average Expense:", round(average_expense, 2), "Rs")
