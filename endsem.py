# x=lambda x,y:x+y
# print(x(2,3))
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))

# fact=lambda n:1 if n==0 else n*fact(n-1)
# print(fact(5))

# num=[1,2,3,4,5,6,7,8,9,10]
# x=map(lambda x:x**2,num)
# print(list(x))
# name='Gopal'
# res=map(lambda x:x,name)
# print(list(res))
# m=filter(lambda x: x%2==0,num)
# print(list(m))
# from functools import reduce
# n=reduce(lambda x,y:x+y,num)
# print(n)


# from math import sqrt 
# p1=[]
# p2=[]
# print("enter x1,y1,z1")
# for i in range(3):
#     p1.append(int(input("enter value ")))
# print("enter x2,y2,z2")
# for i in range(3):
#     p2.append(int(input("enter value ")))
# s=0
# for i in range(3):
#     s=s+((p2[i]-p1[i])**2)
# res=sqrt(s)
# print("distance between two points",res)



# A lambda function in Python is an anonymous, single-line function defined using the lambda keyword. It is used to create small, simple functions on the fly without explicitly defining them using the def keyword.

# syntax:
#     lambda arguments: expression
# add=lambda x,y:x+y
# res=add(2,3)
# print("addition:",res)

# list elements using recursion
# list1=[1,2,3,4,5]
# def display(list1):
#     if not list1:
#         return
#     print(list1[0])
#     display(list1[1:])
# display(list1)

# name='gopal'
# rep=name[len(name)-1]+name[1:len(name)-1]+name[0]
# print(rep)
# n=int(input("enter a year:"))
# if n%400==0 or (n%4==0 and n%100!=0):
#     print("leap year")
# else:
#     print("not a leap year")
# print(5/2)
# print(5//2)
# l=[1,2,1,2,3,4,5,4]
# l.remove(1)
# print(l)

arr=[1,7,6,8]
arr.sort()
arr.insert(2,7)
print(arr)
