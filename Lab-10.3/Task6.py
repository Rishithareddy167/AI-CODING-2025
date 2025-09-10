def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

try:
    score = float(input("Enter the score: "))
    print(f"Grade: {grade(score)}")
except Exception as e:
    print(f"Invalid input: {e}")