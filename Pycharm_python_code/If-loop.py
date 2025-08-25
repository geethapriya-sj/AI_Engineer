n = "Enter a number:"
num = int(input(n))
print(num)
message = "The number is EVEN" if num % 2 == 0 else "The number is ODD"
if not num % 2 == 0:
    print("The number is odd")
else:
    print("The number is even")
if num > 0:
    print("The number is positive")
elif num == 0:
    print("The number is zero")
else:
    print("The number is negative")
print("This statement is always executed")
print(message)
if num > 50 and num % 2 == 0:
    print("The number is greater than 50 and even")