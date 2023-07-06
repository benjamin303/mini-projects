def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(num1, num2):
    return num1 ** num2

def invalid_operation():
    print("Invalid operation")

# Mapping operators to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": pow
}

# Getting user input
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /, **): ")
num2 = float(input("Enter the second number: "))

# Execute the corresponding operation based on the operator
operation = operations.get(operator, invalid_operation)
result = operation(num1, num2)

# Displaying the result
print("Result:", result)