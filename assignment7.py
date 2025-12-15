# Task 1: Read a File and Handle Errors

try:
    # Attempt to open and read the file
    with open("sample.txt", "r") as file:
        print("Reading file content:")
        line_number = 1
        for line in file:
            print(f"Line {line_number}: {line.strip()}")
            line_number += 1

except FileNotFoundError:
    # Error message if file is not found
    print("Error: The file 'sample.txt' was not found.")
