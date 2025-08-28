def factr(n):
    # Convert string to integer if needed
    if isinstance(n, str):
        n = int(n)
    
    if n == 0:
        return 1  # Factorial of 0 is 1
    elif n == 1:
        return 1
    else:
        return n * factr(n - 1)  # Should be n-1, not n-2

print(factr("5"))