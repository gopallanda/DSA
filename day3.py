# functions......
# used for code reusability
# 4types
# syntax def myfn():
#            print("hello")
# fn calling   myfn()
# def area(l, b):

#     print("area of the rectangle is:", l * b)


# length = int(input("enter the length of a rectangle:"))
# breadth = int(input("enter the breadth of a rectangle:"))
# area(length, breadth)

# operand1 = int(input("enter value 1: "))
# operand2 = int(input("enter value 2: "))
# operator = input("enter an operation:+,-,*,/,%: ")

# if operator == "+":
#     print(operand1 + operand2)
# elif operator == "-":
#     print(operand1 - operand2)
# elif operator == "*":
#     print(operand1 * operand2)
# elif operator == "/":
#     print(operand1 / operand2)
# elif operator == "-":
#     print(operand1 % operand2)
# else:
#     print("choose an operator")


# def menuDriven():
#     while True:
#         print("menu")
#         print("1. for '+'")
#         print("2. for '-'")
#         print("3. for '*'")
#         print("4. for '/'")
#         print("5. for '%'")
#         print("6. to exit")
#         choice = input("choose a value between 1-6:")
#         if choice == "1":
#             a = int(input("enter the first value:"))
#             b = int(input("enter the second value:"))
#             add(a, b)

#         elif choice == "2":
#             a = int(input("enter the first value:"))
#             b = int(input("enter the second value:"))
#             sub(a, b)

#         elif choice == "3":
#             a = int(input("enter the first value:"))
#             b = int(input("enter the second value:"))
#             mul(a, b)

#         elif choice == "4":
#             a = int(input("enter the first value:"))
#             b = int(input("enter the second value:"))
#             div(a, b)

#         elif choice == "5":
#             a = int(input("enter the first value:"))
#             b = int(input("enter the second value:"))
#             mod(a, b)

#         elif choice == "6":
#             print("exiting the program")
#             break
#     else:
#         print("invalid choice")


# def add(a, b):
#     print(a + b)


# def sub(a, b):
#     print(a - b)


# def mul(a, b):
#     print(a * b)


# def div(a, b):
#     print(a / b)


# def mod(a, b):
#     print(a % b)


# menuDriven()

# list = ["Delhi", "london", "paris", "NewYork", "Dubai"]
# list2=['Gopal',448,'landa',2022,'nist']

# def count_now(list):
#     for letter in list:
#         if len(letter) > 5:
#             print(letter)

# myList2 = ["Gopal", 448, "landa", 2022, "nist"]


# def count_now(myList2):
#     for letter in myList2:
#         if letter.isdigit():

#             print(letter * 3)
#         else:
#             print(letter + "#")


# myList2 = [
#     "Gopal",
#     "448",
#     "landa",
#     "2022",
#     "nist",
# ]  # isdigit() method only works for strings..

# count_now(myList2)
# o/p

# Gopal#
# 448448448
# landa#
# 202220222022
# nist#


# def find_max(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c


# def main():
#     a = int(input("enter first number:"))
#     b = int(input("enter second number"))
#     c = int(input("enter third number"))
#     d = find_max(a, b, c)
#     print("maximum number is: ", d)


# main
# --------------------------------------------------------------------------
# def isPower(a, b):
#     return a**b


# def main():
#     a = int(input("enter first number:"))
#     b = int(input("enter second number:"))
#     c = isPower(a, b)
#     print(a, "to the power", b, "is:", c)


# main()
# -----------------------------------------------------------------------------


# def sumOfDigits(a):
#     sum = 0


#     while a != 0:
#         r = a % 10
#         a = a / 10
#         sum = sum + r
#     return sum
# def isPalindrome(a):
#     sum = 0
#     temp = a
#     while a != 0:
#         r = a % 10
#         a = a // 10
#         sum = sum * 10 + r
#     if sum == temp:
#         print("the number:", temp, " is a Palindrome")
#     else:
#         print("the number:", temp, " is not a Palindrome")


# def main():
#     a = int(input("enter a number: "))
#     isPalindrome(a)
# main()
# def main():
#     a = int(input("enter a number:"))
#     b = int(sumOfDigits(a))
#     print("sum of digits of the number:", a, "is:", b)


# main()

# --------------------------------------------------------------------------------

# File system.........

# file = open("Sample.txt", "w")
# data = input("enter any text to write:")
# file.write(data)
# file.close()

# file = open("Sample.txt", "r")
# data = file.readlines()[0][0:5]
# file.close()
# print(data)
# -----------------------------------------------------------------------------------
# Deleting file from OS
# import os

# if os.path.exists("sample.txt"):
#     os.remove("sample.txt")
#     print("file is deleted")
# else:
#     print("file not found")


# file = open("hello.txt", "w")
# data = input("enter any text to write:")
# file.write(data)
# file.close()
