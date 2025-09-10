class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment(self, percent):
        self.salary += self.salary * percent / 100

    def display(self):
        print(f"Employee: {self.name}, Salary: {self.salary:.2f}")

try:
    name = input("Enter employee name: ")
    salary = float(input("Enter current salary: "))
    percent = float(input("Enter increment percentage: "))
    emp = Employee(name, salary)
    emp.increment(percent)
    emp.display()
except Exception as e:
    print(f"Invalid input: {e}")