def sort_list(data):
    # Separate numbers and strings
    numbers = [x for x in data if isinstance(x, (int, float))]
    strings = [x for x in data if isinstance(x, str)]
    
    # Sort each type separately
    numbers.sort()
    strings.sort()
    
    # Return combined sorted list (numbers first, then strings)
    return numbers + strings

items = [3, "apples", 1, "banana", 2]
print(sort_list(items))