#Task1: Build a Simple Calculator (CLI)


#takes the input
num1=int(input("Enter first number:"))
operator=input("Enter operation (+,-,*,/):")
num2=int(input("Enter second number:"))

#Performs calculation using if-else
if operator == '+':
    print("Result:",num1+num2)
elif operator == '-':
    print("Result:",num1-num2)
elif operator == '*':
    print("Result:",num1*num2)
elif operator == '/':
    if num2 != 0:
        print("Result:",num1/num2)
    else:
        print("Error:Division by zero is not allowed.")
else:
    print("Invalid operator! Please use +,-,*,/:")
