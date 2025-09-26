file = None
try:
    file=open("customers.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as fnf_error:
    print("File not found error:", fnf_error)
finally:
    print("Executing finally block.")
    if file:
        file.close()
        print("File closed.")

balance = 0

def deposit(Amount):
    global balance
    if Amount <=0:
        raise ValueError("Amount cannot be negative or zero.")
    else:
        balance+=Amount
    print(balance)

def withdraw(Amount):
    global balance
    if Amount > balance:
        raise InsufficientBalanceError("Insufficient balance.")
    else:
        balance-=Amount
class InsufficientBalanceError(Exception):
    pass

deposit(10)
deposit(10)
withdraw(50)