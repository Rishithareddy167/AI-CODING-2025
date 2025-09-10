def find_common(a, b):
    return list(set(a) & set(b))

# Ask for user input
try:
    a = input("Enter the first list of items (comma separated): ").split(',')
    b = input("Enter the second list of items (comma separated): ").split(',')
    # Remove extra spaces
    a = [item.strip() for item in a]
    b = [item.strip() for item in b]
    result = find_common(a, b)
    print(f"Common elements: {result}")
except Exception as e:
    print(f"Invalid input: {e}")