class sru_student:
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False

    def fee_update(self, status):
        self.fee_paid = status

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")

if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    hostel_status = input("Enter hostel status (Hosteller/Day Scholar): ")
    student = sru_student(name, roll_no, hostel_status)
    fee_status = input("Has the fee been paid? (yes/no): ").strip().lower()
    student.fee_update(fee_status == "yes")
    student.display_details()