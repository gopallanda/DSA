# class myClass:
#     num=100
#     def __init__(self,num):
#         print(num) #10
#         print(self.num)  #100
#     def display(self):
#         print("inside class",self.num) #100
# obj=myClass(10)
# obj.display()

# class myClass:
#     num=100
#     def __init__(self,num):
#         self.num=num
#         print(num)# 10
#         print(self.num)  #10
#     def display(self):
#         print("inside class",self.num)  #10
# obj=myClass(10)
# obj.display()

#self keyword is just like this keyword in java 
# it is used to differentiate between class variables and object variables   


# class demo:
#     class_var=0
#     def __init__(self,var):
#         self.class_var+=1
#         vars=var
#         print("object value:",var)
#         print("class_var value",self.class_var)
# obj1=demo(10)
# obj1=demo(20)
# obj1=demo(30)
class Demo:
  
    def __init__(self):
        print("hello")
    def area(self,r):
        print("parent area",r)
class Demo2(Demo):
    def area(self,r):
        print("child area",r)
class Type:
    def __init__(self):
        self.r=Demo()
        self.r.area(4)
obj3=Type()


# obj=Demo()
# obj.area(4)
# obj2=Demo2()
# obj2.area(4)
# print(issubclass(Demo2,Demo))
# print(isinstance(obj,Demo))
# print(isinstance(obj,Demo2))



