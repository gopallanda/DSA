# year = int(input("enter a year: "))
# if year % 4 == 0 and year % 100 != 0:
#     print("distance travelled in this year 1825 km")
# else:
#     print("distance travelled in this year 1831 km")

# a = int(input("enter first number"))
# b = int(input("enter second number"))
# if a % b == 0:
#     print("hi")
# else:
#     print("bye")


# a = int(input("enter year of service"))
# if a > 5:
#     print("eligible for a bonus of 5%")
# else:
#     print("year of service is not suffficient for bonus")


# disc = int(input("enter % of discount:"))
# quantity = int(input("enter the quantity:"))
# cost_per_unit = int(input("enter cost of each quantity:"))
# total_purchase = quantity * cost_per_unit
# net_pay = total_purchase - ((disc / 100) * total_purchase)
# print("total amount purchased:", total_purchase)
# print("amount to pay after discount:", net_pay)
# name = "my name is gopal landa"
# print(name.index("gopal"))
# name.replace("landa", "konda")
# print(name)
# list
# properties of list
# its a group of heterogeneous data
# it is mutable
# represented by [a,b,c,d]
# declaraton
# a = ["Gopal", 448, "M"]
# b = list["gopal"]
# print(a)
# print(b)
# print(type(a))
# print(type(b))


# list['gopal', 667]
# <class 'list'>
# <class 'types.GenericAlias'>
# PS D:\CVML> python leapyear.py
# 11
# my name is gopal landa
# ['Gopal', 448, 'M']
# list['gopal']
# <class 'list'>
# <class 'types.GenericAlias'>
# PS D:\CVML>

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[2:4])
# print(a[3:6])
# [3, 4]
# [4, 5, 6]

# a = ["gopal", 448, False, (45 + 5j), [22, 23, 24, 25], "python"]
# print(a)
# a.append("landa")
# print(a)
# a.insert(3, 10)
# print(a)
# ['gopal', 448, False, (45+5j), [22, 23, 24, 25], 'python']
# ['gopal', 448, False, (45+5j), [22, 23, 24, 25], 'python', 'landa']
# ['gopal', 448, False, 10, (45+5j), [22, 23, 24, 25], 'python', 'landa']

# a.pop(1)
# print(a)
# a.remove("python")
# print(a)
# ['gopal', False, (45+5j), [22, 23, 24, 25], 'python']
# ['gopal', False, (45+5j), [22, 23, 24, 25]]

### empty tuple
# aa = ()
# b = tuple()
# print(type(aa))
# print(type(b))
# ab = (123, 34, "gopal", 879)
# print(ab.count("gopal"))
# print(id(ab))  ## it will give address location of the ab @ 2684613298352


# DICTIONARY IN PYTHON
# stores data in key-value pairs, where key is always unique
# values are cld using keys
# it is not having Index
# represented by DicEg={"Name":"gopal","Age":22, "Gender":"male"}

# d = {}
# e = dict()
# print(type(d))
# print(type(e))
# <class 'dict'>
# <class 'dict'>

# info = {
#     "Name": "Gopal",
#     "age": 22,
#     "Branch": "IT",
#     "rollno": 448,
#     "Tech": ["html", "css", "js", "c", "java", "python"],
# }
# print(info)
# {'Name': 'Gopal', 'age': 22, 'Branch': 'IT', 'rollno': 448, 'Tech': ['html', 'css', 'js', 'c', 'java', 'python']}

# print(info["Tech"][2])
# print(info["age"])
# print(info.keys())
# print(info.items())


# outputs
# js
# 22
# dict_keys(['Name', 'age', 'Branch', 'rollno', 'Tech'])
# dict_items([('Name', 'Gopal'), ('age', 22), ('Branch', 'IT'), ('rollno', 448), ('Tech', ['html', 'css', 'js', 'c', 'java', 'python'])])
###   SETS.......
# unordered collection of unique elements
# it does not support indexing
# heterogeneous

### empty set
# s = set()
# print(type(s))
# x = {1, 2, 3, 4, 5}
# y = {1, 4, 5, 8, 9}
# print(x.union(y))
# print(x.intersection(y))
# print(x.difference(y))
# print(x & y)
# print(x | y)

# outputs

# {1, 2, 3, 4, 5, 8, 9}
# {1, 4, 5}
# {2, 3}
# {1, 4, 5}
# {1, 2, 3, 4, 5, 8, 9}


### LIST................

mylist = []
size = int(input("how any elements do you want to enter?"))
for i in range(size):
    data = int(input())
    mylist.append(data)
print("alternate elements are: ")
for i in range(size):
    print(mylist[i])
high = mylist[0]
for i in range(size):
    if mylist[i] >= high:
        high = mylist[i]
print("maximum element is:", high)
print("maximum element is ", max(mylist))
print("minimum element", min(mylist))
print("reverse of the list..:")

while size > 0:
    print(mylist[size - 1])
    size = size - 1
mylist2 = []
size2 = int(input("enter the number of elements of second list"))
for i in range(size2):
    data2 = int(input())
    mylist2.append(data2)
print("elements of second list")
for i in range(size2):
    print(mylist2[i])
for i in range(size):
    mylist[i].concat(mylist2[i])
print(mylist)
