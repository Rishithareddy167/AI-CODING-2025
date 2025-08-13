# Step 1: Vague prompt
# Generate python code to calculate power bill

# Step 2: Clarify requirements
# Let's assume the user wants to input the number of units consumed and the rate per unit.

# Step 3: Further improve by handling invalid input and providing a detailed bill

def calculate_power_bill(units_consumed, rate_per_unit):
    """
    Calculate the total power bill based on units consumed and rate per unit.
    Args:
        units_consumed (float): Number of electricity units consumed.
        rate_per_unit (float): Cost per unit.
    Returns:
        float: Total bill amount.
    """
    if units_consumed < 0 or rate_per_unit < 0:
        raise ValueError("Units consumed and rate per unit must be non-negative.")
    return units_consumed * rate_per_unit

def main():
    try:
        units = float(input("Enter the number of units consumed: "))
        rate = float(input("Enter the rate per unit: "))
        total = calculate_power_bill(units, rate)
        print(f"\n--- Power Bill ---")
        print(f"Units Consumed: {units}")
        print(f"Rate per Unit: {rate}")
        print(f"Total Bill: {total}")
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()

