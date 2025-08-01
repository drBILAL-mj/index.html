# Basic Calculator program
# Ask the user to input two numbers
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))

# Ask the user to input a mathematical operator
operator = input("Enter the operation (+, -, *, /):")

# Perform the operation
if operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is undefined.")

else:
    print("Invalid operator! Use +, -, *, or /")