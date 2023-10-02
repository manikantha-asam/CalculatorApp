import math

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    else:
        return x / y

# Function to calculate exponentiation
def exponentiate(x, y):
    return x ** y

# Function to calculate square root
def square_root(x):
    if x < 0:
        return "Invalid input. Cannot calculate square root of a negative number"
    else:
        return math.sqrt(x)

# Function to calculate modulus
def modulus(x, y):
    if y == 0:
        return "Cannot calculate modulus with zero as the divisor"
    else:
        return x % y

while True:
    # Display the menu
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'exponentiate' for exponentiation")
    print("Enter 'square_root' for square root")
    print("Enter 'modulus' for modulus")
    print("Enter 'quit' to end the program")

    # Take user input
    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "exponentiate", "square_root", "modulus"):
        if user_input != "square_root":
            num1 = float(input("Enter first number: "))
        if user_input != "exponentiate" and user_input != "square_root":
            num2 = float(input("Enter second number: "))

        if user_input == "add":
            print("Result: ", add(num1, num2))
        elif user_input == "subtract":
            print("Result: ", subtract(num1, num2))
        elif user_input == "multiply":
            print("Result: ", multiply(num1, num2))
        elif user_input == "divide":
            print("Result: ", divide(num1, num2))
        elif user_input == "exponentiate":
            print("Result: ", exponentiate(num1, num2))
        elif user_input == "square_root":
            num1 = float(input("Enter a number: "))
            print("Result: ", square_root(num1))
        elif user_input == "modulus":
            print("Result: ", modulus(num1, num2))
    else:
        print("Invalid input. Please try again.")
