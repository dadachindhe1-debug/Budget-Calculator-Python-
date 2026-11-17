# Pocket Money and Monthly Savings Calculator

budget = float(input("Enter your monthly budget (in Rs): "))
expense = float(input("Enter your total monthly expense (in Rs): "))

savings = budget - expense

print("---------------------------------")

if savings > 0:
    print("Congratulations! Your monthly savings:", savings, "Rs")
    print("In 1 year, you will save:", savings * 12, "Rs!")
elif savings == 0:
    print("Your budget and expenses are equal. Zero savings.")
else:
    print("Warning! Your expenses exceeded your budget by:", abs(savings), "Rs.")
