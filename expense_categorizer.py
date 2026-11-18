# AI Smart Expense Categorizer using Python Dictionary (Version 4)

expenses = {}  # Dictionary

print("--- Welcome to AI Smart Expense Categorizer ---")

while True:
    category = input("Where did you spend? (e.g., Food, Travel, Books): ").strip().capitalize()
    amount = float(input(f"Enter amount spent on {category} (in Rs): "))
    
    # 
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
        
    choice = input("Add another expense? (yes/no): ")
    if choice.strip().lower() != 'yes':
        break

print("\n--- Detailed Expense Report ---")
for cat, amt in expenses.items():
    print(f"{cat}: {amt} Rs")

#
highest_category = max(expenses, key=expenses.get)
print("---------------------------------")
print(f"AI Insight: You spent the most on '{highest_category}' ({expenses[highest_category]} Rs)!")