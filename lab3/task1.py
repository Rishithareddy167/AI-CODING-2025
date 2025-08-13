from functools import reduce

# 1. Iterative version
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 2. Recursive version
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# 3. One-liner using functools.reduce
factorial_lambda = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)

# === Testing all versions ===
test_value = 5
print("Factorial of", test_value)
print("Iterative: ", factorial_iterative(test_value))
print("Recursive: ", factorial_recursive(test_value))
print("Lambda/Reduce: ", factorial_lambda(test_value))

