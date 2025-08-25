expenses = [1200, 1300, 1250, 1450, 2000]

total_Expense = 0
print("Using direct iteration:")
for expense in expenses:
    print(expense)
    total_Expense = total_Expense + expense
print("Total Expense:", total_Expense)

total_Expense = 0
print("Using index:")
for i in range(len(expenses)):
    print(f"Month {i + 1}: {expenses[i]}")
    total_Expense +=  expenses[i]
print("Total Expense:", total_Expense)

total_Expense =0
print("Using enumerate:")
for month,expense in enumerate(expenses,start=1):
    print(f"Month {month}: {expense}")
    total_Expense += expense
print("Total Expense:", total_Expense)

