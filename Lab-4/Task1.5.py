def count_lines_in_file(example):
    """
    Reads a .txt file and returns the number of lines.

    Few-shot examples (inputs -> outputs):
    - "notes.txt" -> 12
    - "empty.txt" -> 0
    - "C:/data/logs/today.txt" -> 347

    Args:
        filename (str): The path to the .txt file.

    Returns:
        int: The number of lines in the file.
    """
    with open(example, 'r', encoding='utf-8') as file:
        return sum(1 for _ in file)

# Interactive usage
if __name__ == "__main__":
    print("File Line Counter")
    print("=" * 18)
    user_path = input("Enter the path to a .txt file (e.g., sample.txt): ").strip().strip('"')
    if not user_path:
        print("No input provided.")
    elif not user_path.lower().endswith('.txt'):
        print("Please provide a .txt file.")
    else:
        try:
            lines = count_lines_in_file(user_path)
            print(f"Number of lines in '{user_path}': {lines}")
        except FileNotFoundError:
            print(f"File not found: {user_path}")
        except PermissionError:
            print(f"Permission denied: {user_path}")
        except UnicodeDecodeError:
            print(f"Encoding error while reading: {user_path}")

