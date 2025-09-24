class Student:
    """
    A class to represent a student with their personal details and academic marks.
    
    Attributes:
        name (str): The student's name
        age (int): The student's age
        marks (list): A list of the student's marks for different subjects
    """
    
    def __init__(self, name, age, *marks):
        """
        Initialize a Student object.
        
        Args:
            name (str): The student's name
            age (int): The student's age
            *marks: Variable number of marks for different subjects
        """
        self.name = name
        self.age = age
        self.marks = list(marks)
    
    def details(self):
        """
        Print the student's personal details in a formatted way.
        """
        print(f"Student Details:")
        print(f"  Name: {self.name}")
        print(f"  Age: {self.age}")
    
    def total(self):
        """
        Calculate the total of all marks.
        
        Returns:
            int: The sum of all marks
        """
        return sum(self.marks)
    
    def average(self):
        """
        Calculate the average of all marks.
        
        Returns:
            float: The average of all marks
        """
        return self.total() / len(self.marks) if self.marks else 0

# Example usage:
student = Student("Alice", 20, 85, 90, 95)
student.details()
print(f"Total Marks: {student.total()}")
print(f"Average Marks: {student.average():.2f}")