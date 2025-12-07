# Task 1: Perform Basic Mathematical Operations

# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division safely
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Remove .0 from whole numbers
# (simple method for beginners)
if addition.is_integer():
    addition = int(addition)

if subtraction.is_integer():
    subtraction = int(subtraction)

if multiplication.is_integer():
    multiplication = int(multiplication)

# For division, convert only if it's not an error message
if division != "Undefined (division by zero)" and isinstance(division, float):
    if division.is_integer():
        division = int(division)

# Print results
print("\nAddition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
