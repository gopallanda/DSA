class GrandFather:
    def __init__(self,GrandfatherName):
        self.GrandfatherName=GrandfatherName
class Father(GrandFather):
    def __init__(self,FatherName,GrandfatherName):
        self.FatherName=FatherName
        GrandFather.__init__(self,GrandfatherName)
class Son(Father):
    def __init__(self,sonName,FatherName,GrandfatherName):
        self.sonName=sonName
        Father.__init__(self,FatherName,GrandfatherName)
    def print(self):
        print("Grand Father Name:",self.GrandfatherName)
        print("Father Name:",self.FatherName)
        print("Son Name:",self.sonName)
        
obj=Son("Mahendra Bahubali","Amarendra Bahubali","Vijayendra Bahubali")

obj.print()