def discount(price, category):
    if category == "student":
        return price * 0.9 if price > 1000 else price * 0.95
    return price * 0.85 if price > 2000 else price

# Ask for user input
try:
    price = float(input("Enter the price: "))
    category = input("Enter the category (student/other): ").strip().lower()
    result = discount(price, category)
    print(f"Discounted price: {result:.2f}")
except Exception as e:
    print(f"Invalid input: {e}")