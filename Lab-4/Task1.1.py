def is_leap_year(year):
    """
    Checks whether the given year is a leap year.

    Args:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Test the function with some example years
if __name__ == "__main__":
    test_years = [2000, 2020, 2024, 1900, 2023, 2100]
    
    print("Leap Year Checker")
    print("=" * 20)
    
    for year in test_years:
        result = is_leap_year(year)
        status = "is" if result else "is not"
        print(f"{year} {status} a leap year")
