# class obj1:
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,u):
#         return self.x+u.x
# a=obj1(2)
# b=obj1(3)
# c=obj1(4)
# print(a+b) 5
# print(b+c) 7
#print(a+b+c) #type Error


# class obj1:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self,u):
#         return self.x+u.x,self.y+u.y
# a=obj1(2,1)
# b=obj1(3,2)
# print(a+b) (5,3)

# class Demo:
#     def __init__(self,x):
#         self.x=x
#     def __sub__(self,u):
#         return self.x-u.x
# obj1=Demo(10)
# obj2=Demo(5)
# print(obj1-obj2) 5
# print(obj2-obj1) -5

class Demo:
    def __init__(self,x):
        self.x=x
    def __gt__(self,u):
       if self.x>u.x:
           return True
       else:
           return False
obj1=Demo(10)
obj2=Demo(5)
if obj1>obj2:
    print("ob1>obj2")
else:
    print(obj1<obj2)