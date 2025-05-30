class Employee:
    def personalDetails(self,id,name,age,bg):
        print("Details of employee ID: ",id)
        print("Name:",name)
        print("Age:",age)
        print("Blood Group:",bg)
    def Salary(self,sal):
        print("salary:",sal)
class Emp1(Employee):
   pass
class Emp2(Employee):
   pass
class Emp3(Employee):
   pass
class Emp4(Employee):
   pass
class Emp5(Employee):
   pass
e1=Emp1()
e1.personalDetails(111,"Ram",20,"A+")
e1.Salary(25000)

e2=Emp2()
e2.personalDetails(112,"Sam",21,"B+")
e2.Salary(25000)

e3=Emp3()
e3.personalDetails(113,"Gani",22,"AB+")
e3.Salary(25000)

e4=Emp4()
e4.personalDetails(114,"Dev",23,"A-")
e4.Salary(60000)

e5=Emp5()
e5.personalDetails(115,"Bunny",24,"0+")
e5.Salary(25000)