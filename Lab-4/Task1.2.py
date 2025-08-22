def cm_to_inches(cm):
    """
    Converts centimeters to inches.

    Args:
        cm (float): The length in centimeters.

    Returns:
        float: The length in inches.
    """
    if cm < 0:
        raise ValueError("Length cannot be negative")
    return cm / 2.54

def inches_to_cm(inches):
    """
    Converts inches to centimeters.

    Args:
        inches (float): The length in inches.

    Returns:
        float: The length in centimeters.
    """
    if inches < 0:
        raise ValueError("Length cannot be negative")
    return inches * 2.54

# Test the functions with various examples
if __name__ == "__main__":
    print("Length Conversion Calculator")
    print("=" * 30)
    
    # Test cases for cm to inches
    test_cm_values = [10, 25.4, 50, 100]
    print("\nCentimeters to Inches:")
    for cm in test_cm_values:
        inches = cm_to_inches(cm)
        print(f"{cm} cm = {inches:.4f} inches")
    
    # Test cases for inches to cm
    test_inch_values = [1, 5, 10, 20]
    print("\nInches to Centimeters:")
    for inches in test_inch_values:
        cm = inches_to_cm(inches)
        print(f"{inches} inches = {cm:.2f} cm")
    
    # Interactive example
    print(f"\nExample: 10 centimeters is equal to {cm_to_inches(10):.4f} inches")
