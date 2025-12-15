# Take user input and write to file
text = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to output.txt.")

# Take additional input and append to the same file
additional_text = input("Enter additional text to append: ")

with open("output.txt", "a") as file:
    file.write(additional_text + "\n")

print("Data successfully appended.")

# Read and display final content of the file
print("\nFinal content of output.txt:")

with open("output.txt", "r") as file:
    print(file.read())
