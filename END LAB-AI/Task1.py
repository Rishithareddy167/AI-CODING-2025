class Employee_Payroll:
    """
    Employee Payroll System
    -----------------------
    Calculates:
        - PF  : 12% of basic salary
        - Deductions : user-specified
        - Net Salary : basic - (PF + deductions)
    """

    def __init__(self, emp_id, emp_name, basic_salary, deductions):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.basic_salary = basic_salary
        self.deductions = deductions

    def calculate_pf(self):
        """Returns 12% PF of basic salary."""
        return self.basic_salary * 0.12

    def calculate_net_salary(self):
        """Returns final salary after PF + deductions."""
        pf = self.calculate_pf()
        net = self.basic_salary - (pf + self.deductions)
        return net

    def display_payroll(self):
        """Prints payroll details."""
        pf = self.calculate_pf()
        net_salary = self.calculate_net_salary()

        print("----------- Employee Payroll Details -----------")
        print(f"Employee ID        : {self.emp_id}")
        print(f"Employee Name      : {self.emp_name}")
        print(f"Basic Salary       : {self.basic_salary}")
        print(f"PF (12%)           : {pf}")
        print(f"Deductions         : {self.deductions}")
        print(f"Net Salary         : {net_salary}")
        print("------------------------------------------------\n")


# --------------------------------------------------------
# TEST CASES (AI-Assisted sample)
# --------------------------------------------------------

# Test Case 1
emp1 = Employee_Payroll(
    emp_id=101,
    emp_name="Rishitha",
    basic_salary=50000,
    deductions=2000
)
emp1.display_payroll()

# Test Case 2
emp2 = Employee_Payroll(
    emp_id=102,
    emp_name="Arjun",
    basic_salary=30000,
    deductions=1500
)
emp2.display_payroll()

# Test Case 3
emp3 = Employee_Payroll(
    emp_id=103,
    emp_name="Meena",
    basic_salary=45000,
    deductions=1000
)
emp3.display_payroll()
