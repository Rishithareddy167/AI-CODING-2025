def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test cases
print("Input: 5 → Output: Factorial =", factorial(5))  # Output: 120
print("Input: 0 → Output: Factorial =", factorial(0))  # Output: 1