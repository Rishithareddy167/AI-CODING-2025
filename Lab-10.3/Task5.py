def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

try:
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))
    print(div(a, b))
except Exception as e:
    print(f"Invalid input: {e}")