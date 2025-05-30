# a = 10
# b = "Ram"
# c = "h"
# print(type(a))
# print(type(b))
# print(type(c))
# output
# <class 'int'>
# <class 'str'>
# <class 'str'>
# -----------------------------------------------------------------------------------
# identity operator
# a = 10
# b = 10
# print(a is b)
# print(a is not b)
# b = 11
# print(a is b)

# membership operator
# a = "i love my india"
# print("india" in a)
# print("gopal" in a)
# ----------------------------------------------------------------------------------------

# eval() method to accept any type of value
# var = eval(input("enter: "))
# print(type(var))
# print(var)

# o/p-1
# enter: 10
# <class 'int'>
# 10

# o/p-2
# enter: 10.5
# <class 'float'>
# 10.5

# o/p-3
# enter: "gopal"
# <class 'str'>
# gopal
# ------------------------------------------------------------------------

# while loop

# password = "nist"
# inputpw = input("enter password: ")
# while password != inputpw:
#     inputpw = input("enter password :")
# else:
#     print("unlocked..!")


# o/p:
# enter password: gopal
# enter password :ram
# enter password :seeta
# enter password :hy
# enter password :nist
# unlocked..!


# positive = negative = zeroes = 0
# while 1:
#     num = int(input("enter a number: "))
#     if num == -1:
#         break
#     elif num > 0:
#         positive += 1
#     elif num == 0:
#         zeroes += 1
#     else:
#         negative += 1
# print("no of +ve integers entered : ", positive)
# print("no of -ve integers entered : ", negative)
# print("no of 0 's  entered : ", zeroes)


# enter a number: 1
# enter a number: 2
# enter a number: 5
# enter a number: 7
# enter a number: -8
# enter a number: -4
# enter a number: -5
# enter a number: 0
# enter a number: 0
# enter a number: 0
# enter a number: -1
# no of +ve integers entered :  4
# no of -ve integers entered :  3
# no of 0 's  entered :  3
# ------------------------------------------------------------------------------
