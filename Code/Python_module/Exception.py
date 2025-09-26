x = input("Enter number x:")
y = input("Enter number y:")

d = 0
try:
    d = int(x)/int(y)
    #a= 'my stirng'+56
except ZeroDivisionError as ze:
    print("Division by zero is not allowed.",ze)
    d = -1
except TypeError as te:
    print("Type error occurred.",te)
    d = -1
except Exception as e:
    print("Some other error occurred.", e)
finally:
    print('finally block executed.')
print(d)