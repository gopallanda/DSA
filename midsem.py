# a=10
# b=10
# print(id(a))
# print(id(b))
# print(a is b)
# print(a is not b)
# aa="i am iron man"
# bb="gopal"
# print(bb in aa)
# print(bb not in aa)
# x=10
# def eg():

#    y=34
#    print(x)
# eg()
# print(x)
# print(y)

# def arith(a,b):
#     summ=a+b
#     sub=a-b
#     div=a/b
#     mod=a%b
#     return summ,sub,div,mod
# test=arith(20,10)
# print(test)
# for i in test:
#     print(i)

# def dis(str):
#     def msg():
#         return "hi"
#     res=msg()+str
#     return res
# st=dis("Roy")
# print(st)
# def add(f,*arg):
#     sum=0
#     for i in  arg:
#         sum=sum+i
#     print(f+sum)
#     print(locals())
#     print(arg)
# add(1,2)
# add(1,2,3,4,5,6)
# print(globals())


# sum = lambda x,y : x+y
# print(sum(4,8))

# from math import sqrt,pi
# def area(r):
#     print(pi*r*r)
#     print(sqrt(16))
# area(2)


# item={1,2,3,4,5}
# res=map(lambda x:x*x,item)
# print(list(res))
# print(type(res))

# item=[1,2,3,4,5,6]

# import functools
# item=[1,2,3,4,5,6]
# def add(x,y):
#     return x+y
# res=functools.reduce(add,item)
# print(res)
# list=[1,2,3,4,5]
# res=functools.reduce(lambda x,y:x+y,list)
# print(res)
# import re
# name="gopala gopala gopala"
# x='s'
# print(name.replace('g',x))
# p='g'
# r='s'
# print(re.sub(p,r,name))
# lists=[1,2,3,4,5]
# print(lists.pop(0))
# print(lists)
# print(lists.remove(4))
# print(lists)
# lists.insert(2,5)
# lists.append(5)
# print(lists)
# cubes=[i**3 for i in range(5)]
# print(cubes)
# name="gopal"
# l=len(name)
# swap=name[l-1]+name[1:l-1]+name[0]
# print(swap)
# arr=[1,2,3,4,5]
# print(arr)
# arr.insert(0,8)
# print(arr)

# def isSubset( a1, a2, n, m):
#     for x in a2:
#         if x not in a1:
#           return "no"
#         else:
#           return "No"

# def isSubset( a1, a2, n, m):
#     count=0
#     for i in a2:
#         if i in a1:
#             count=count+1
#             # index=a1.index(a2[i])
#             a1.remove(i)
#     if count==m:
#         return "Yes"
#     else:
#         return "No"
# from collections import Counter

# def isSubset(a1, a2, n, m):
#     # Count the frequency of elements in a1
#     count_a1 = Counter(a1)
#     print(count_a1)

#     # Check if every element in a2 can be matched with a1's counts
#     for element in a2:
#         if count_a1[element] > 0:
#             count_a1[element] -= 1
#             print(count_a1[element])# Use one occurrence of the element
#         else:
#             return "No"  # If element is not available, return "No"

#     return "Yes"

# a1=[1,2,4,3,1,2,5,4,3,2,1,2]
# a2=[1,2,3,3]
# n=len(a1)
# m=len(a2)
# # fi=a1.index(a2[1])
# # print(fi)
# print(isSubset(a1,a2,n,m))
# file=open("textfile.txt","a")
# file.write(" \nHope all are good\n")
# # print(file.read())
# file.close()

# file=open("textfile.txt","r+")
# file.write(" \nHope all are good\n and well\n")
# print(file.read())
# file.close()

# file=open("textfile.txt","r")
# print(file.read(10))
# file.close

# file = open("textfile.txt", "a")
# # a="gopala krishna "
# file.write("Hello Welcome to the World of Python")
# file.close()

# file=open("textfile.txt","a+")
# file.write(" hare krishna\n ")
# file.close()
# print(file.closed)

file = open("textfile.txt", "r+")
file.write("Hello Welcome to the World of Python")
line = file.readline()
words = line.split()
print(words)
file.close()
