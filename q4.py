class Employee:
    def __init__(self, empno, name, designation):
        self.empno = empno
        self.name = name
        self.designation = designation


class Qualification(Employee):
    def __init__(self, empno, name, designation, UG, PG, experience):
        super().__init__(empno, name, designation)
        self.UG = UG
        self.PG = PG
        self.experience = experience


class Salary(Qualification):  # class Salary(Qualification,Employee): gives same res
    def __init__(self, empno, name, designation, UG, PG, experience):
        super().__init__(empno, name, designation, UG, PG, experience)

    def details(self):
        print("Details of the employee:", self.empno)
        print("Name:", self.name)
        print("Designation:", self.designation)
        print("qualification:", "UG" if self.UG == True else "PG")
        print("Experience:", self.experience, "years")

    def Increment(self):
        increment = 0
        if self.UG == True:
            increment += self.experience
            print("Increment:", increment, "% Annually")
        else:
            increment += self.experience * 2
            print("Increment:", increment, "% Annually")


obj = Salary(123, "Ram", "Software Engineer", True, False, 5)
obj.details()
obj.Increment()
