# The data members declared inn a parent class can by accessed by the child class using self.datamember, and a variable that is declared inside an init method of a class can be accessed by any method inside the class
class Student:
    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

# Derived class for handling fees
class Fees(Student):
    def __init__(self, rollno, name, fees=0):
        super().__init__(rollno, name)
        self.fees = fees

    def submit_fee(self, amount):
        self.fees += amount
        print("Fee of",amount,"submitted successfully.")

    def generate_receipt(self):
        print("Receipt for",self.name,"Roll No:", self.rollno)
        print("Total fees submitted:",self.fees)


class Result(Student):
    def __init__(self, rollno, name, marks, grade):
        super().__init__(rollno, name)
        self.marks = marks
        self.grade = grade

    def display_result(self):
        print("Result for", self.name,"Roll No:",self.rollno)
        print("Marks Obtained:", self.marks)
        print("Grade:",self.grade)

# Example usage
student1 = Fees(101, "Sweety")
student1.submit_fee(5000)
student1.generate_receipt()

student2 = Result(102, "Sunita", 85, "A")
student2.display_result()
