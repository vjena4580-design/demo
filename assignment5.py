# Task 1: Calculate Factorial Using a Function

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Taking input from the user
number = int(input("Enter a number: "))

# Printing the factorial result
print(f"\nFactorial of {number} is: {factorial(number)}")
