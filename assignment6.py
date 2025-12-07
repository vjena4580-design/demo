import math

# Asking the user for a number
number = float(input("Enter a number: "))

# Performing calculations using the math module
square_root = math.sqrt(number)
logarithm = math.log(number)      # Natural log (base e)
sine_value = math.sin(number)     # Number treated as radians

# Displaying the results
print(f"\nSquare root: {square_root}")
print(f"Logarithm: {logarithm}")
print(f"Sine: {sine_value}")
