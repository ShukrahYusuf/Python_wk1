# Simple Basic Calculator Program

# Ask user for two numbers (floats to support decimals)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask user for operation
operation = input("Enter the operation (+, -, *, /, **): ")

# Perform calculation based on operation
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Handle division by zero
    if num2 == 0:
        result = "undefined (cannot divide by zero)"
    else:
        result = num1 / num2
elif operation == "**":
    result = num1 ** num2
else:
    result = "Invalid operation"

# Display result
print(f"{num1} {operation} {num2} = {result}")
