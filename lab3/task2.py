def sort_numbers(numbers):
    # Using Bubble Sort algorithm
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

# Example usage:
print(sort_numbers([5, 2, 9, 1, 5, 6]))  # Output: [1, 2, 5, 5, 6, 9]
