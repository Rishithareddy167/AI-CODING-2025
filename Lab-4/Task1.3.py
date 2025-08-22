def format_name(full_name):
    """
    Formats a full name as "Last, First".
    
    Args:
        full_name (str): The full name in "First Last" format.
        
    Returns:
        str: The formatted name as "Last, First".
        
    Examples:
        >>> format_name("John Smith")
        'Smith, John'
        >>> format_name("Alice Johnson")
        'Johnson, Alice'
        >>> format_name("Mary Ann Lee")
        'Lee, Mary Ann'
    """
    parts = full_name.strip().split()
    if len(parts) < 2:
        raise ValueError("Full name must contain at least first and last name")
    first = " ".join(parts[:-1])
    last = parts[-1]
    return f"{last}, {first}"

# Example usage
if __name__ == "__main__":
    print(format_name("John Smith"))        # Output: Smith, John
    print(format_name("Alice Johnson"))     # Output: Johnson, Alice
    print(format_name("Mary Ann Lee"))      # Output: Lee, Mary Ann
