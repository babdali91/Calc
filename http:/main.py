# A simple Python program to add two numbers

def add_numbers(a, b):
    return a + b

# Input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the sum
result = add_numbers(num1, num2)

# Display the result
print(f"The sum of {num1} and {num2} is: {result}")
