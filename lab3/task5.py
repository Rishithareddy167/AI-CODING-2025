# 1. Vague Prompt Version
def convert_temperature(temp):
    return temp * 1.8 + 32

print(convert_temperature(25))  # Output: 77.0


# 2. Simple & Clear Version
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

print(celsius_to_fahrenheit(25))  # Output: 77.0


# 3. Detailed & Robust Version
def celsius_to_fahrenheit_detailed(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    
    Parameters:
    celsius (float): Temperature in Celsius
    
    Returns:
    float: Temperature converted to Fahrenheit
    
    Raises:
    ValueError: If the input is not a number
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    return celsius * 9 / 5 + 32

print(celsius_to_fahrenheit_detailed(25))  # Output: 77.0
