def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        print("File read successfully")
        return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError as e:
        print(f"IOError while reading file '{filename}': {e}")
    return None

if __name__ == "__main__":
    filename = "example.txt"
    content = read_file(filename)
    if content is not None:
        print("File content:")
        print(repr(content))  # <--- Add this
