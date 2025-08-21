def calculate_marks(marks):
    if marks>=90:
        return "A"
    elif marks>=75:
        return "B"
    elif marks>=60:
        return "C"
    else:
        return "F"
def student_marks(name,marks,roll_no):
    print(f"Name: {name}, Marks: {marks}, Roll No: {roll_no}")
    print (f"Garde:",calculate_marks(marks))
    print("-----------------------------")

    # INSERT_YOUR_CODE
def main():
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        while True:
            try:
                marks = float(input("Enter marks: "))
                break
            except ValueError:
                print("Please enter a valid number for marks.")
        student_marks(name, marks, roll_no)

if __name__ == "__main__":
    main()

