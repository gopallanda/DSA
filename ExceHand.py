# a=int(input("enter a:"))
# b=int(input('enter b:'))
# d=[1,2,3,4,5]
# try:
#     c=a/b
#     print(c)
#     print(d[10])
# except ZeroDivisionError:
#     print("b value should not be 0")
# except IndexError:
#     print("array index out of bounds..")

# a=int(input('enter a :'))
# b=int(input('enter b :'))
# c=[1,2,3,4,5]
# try:
#     d=a/b
#     try:
#         print(c[10])
#     except IndexError:
#         print("index error")
# except ZeroDivisionError:
#     print("b should not be zero")

# try:
#     n=int(input("age:"))
#     if n<18:
#         raise ValueError("value wrong")
#     else:
#         print(n)    
# except ValueError as e:
#     print(e)

# class ValueTooSmallError(Exception):
#     """ hi hello iam value too small"""
#     pass
# class ValueTooLargeError(Exception):
#     """ hi hello iam value too small"""
#     pass
# while(True):
#     try:
#         n=int(input("enter a number:"))
#         if n<18:
#             raise ValueTooSmallError
#         elif n>18:
#             raise ValueTooLargeError
#         else:
#             print(n)
#         break
#     except ValueTooSmallError:
#         print("value too small")
#     except ValueTooLargeError:
#         print("value too large")

# class ageLess(Exception):
#     pass
# while(True):
#     try:
#         age=int(input("enter age:"))
#         if age<18:
#             raise ageLess
#         else:
#             print("you are eligible")
#         break
#     except ageLess:
#         print("age is not sufficient")
    
i = 1
while True:
 if i%3 == 0:
  break
 print(i)
 i+=1
 o/p=
 1
 2
 
print(min(max(False,-4,-3),2,4))
l=[1,0,2,0,'hello'," ",[]]
print(list(filter(bool,l))) # [1, 2, 'hello', ' ']

t1=(1,2,(2,(3,3,8)))
print(len(t1[2][1]))
list1 = [2, 3, 4, 5, 6]
list1[:-2]
print(list1) #[2,3,4,5,6]

from functools import reduce
list1=[50,67,80,98,65,58]
res=reduce(lambda x,y:x+y,list1)
print("average=",res//len(list1))