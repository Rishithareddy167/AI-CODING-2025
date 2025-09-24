"""
Program to calculate squares of numbers from 1 to 10.
Demonstrates list comprehension as a more Pythonic approach.
"""

# Define the range of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate squares using list comprehension (more Pythonic)
squares = [num ** 2 for num in numbers]

# Display results with better formatting
print("Original numbers:", numbers)
print("Squared numbers: ", squares)
print(f"Sum of squares: {sum(squares)}")