# Reverse a Number
# num = int(input("enter a number: "))
# s = 0
# while num != 0:
#     r = num % 10
#     s = s * 10 + r
#     num = num // 10
# print("reverse of the number :", s)
# ------------------------------------------------------------------------------

# Sum of digits
# num = int(input("enter a number: "))
# s = 0
# while num != 0:
#     r = num % 10
#     s = s + r
#     num = num // 10
# print("sum of digits  :", s)
# ---------------------------------------------------------------------------------

# palindrome number
# num = int(input("enter a number: "))
# s = 0
# g = num
# while num != 0:
#     r = num % 10
#     s = s * 10 + r
#     num = num // 10
# if s == g:
#     print("palindrome number")
# else:
#     print("not a palindrome number")
# -----------------------------------------------------------------------------------

# decimal to binary equivalent
# n = int(input("enter a decimal number:"))
# if n == 0:
#     print("the binary value of 0 is: ", n)
# else:
#     bd = ""
#     g = n
#     while n != 0:
#         r = n % 2
#         bd = str(r) + bd
#         n = n // 2
#     print("the binary value of ", g, "is:", bd)
# -----------------------------------------------------------------------------------------

# binary to decimal
# n = int(input("enter a binary number:"))
# if n == 0:
#     print("the decimal value of 0 is: ", n)
# else:
#     d = 0
#     g = n
#     i = 0
#     while n != 0:
#         r = n % 10

#         d = d + (r * (2**i))
#         i = i + 1
#         n = n // 10
#     print("the decimal value of ", g, "is:", d)
# ------------------------------------------------------------------------------------------
# hcf and gcd

# The Euclidean algorithm is a method to find the Greatest Common Divisor (GCD) or Highest Common
#  Factor (HCF) of two numbers. It works based on the principle that the GCD of two numbers also
#  divides their difference.

# Steps of the Euclidean Algorithm:
# 1) Divide the larger number by the smaller number and find the remainder.
# 2) Replace the larger number with the smaller number, and replace the smaller number with the
#    remainder.
# 3) Repeat the process until the remainder is 0. At this point, the smaller number (which now
#   doesn't change) will be the GCD of the original two numbers.


# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# if a > b:
#     gr = a
# else:
#     gr = b
# i = 1
# while i <= gr:
#     if a % i == 0 and b % i == 0:
#         hcf = i
#     i = i + 1
# print("the hcf or gcd  of ", a, b, "is:", hcf)
# print("lcm of", a, b, "is:", a * b // hcf)
# -------------------------------------------------------------------------------------------
# n = int(input("enter the number of terms:"))
# sum = 0
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
#     sum = sum + i / fact

# print(sum)
# 1/1!+2/2!+3/3!+....
# -------------------------------------------------------------------------------------------
# -1/2+1/3-1/4+1/5....
# n = int(input("enter the number of terms:"))
# s = 0
# fact = 1
# sign = '-'
# for i in range(1, n + 1):
#    print(f"{sign}")
# -------------------------------------------------------------------------------------------
#  LEAP YEAR
# yr=int(input("enter the year:"))
# if yr%4==0 or (yr%100==0 and yr%400!=0):
#     print(f"{yr} is a leap year😎")
# else:
#     print(f"{yr} is a not a leap year😒")
# -------------------------------------------------------------------------------------------
# roots of a QE
# from math import sqrt
# a=int(input("enter X^2 coefficient:"))
# b=int(input("enter X coefficient:"))
# c=int(input("enter constant value:"))
# d=(b**2)-(4*a*c)
# if d==0:
#     x1=-b/2*a
#     print("the quadratic equation has 2 equal real roots:",x1,x1)
# elif d>0:
#     x1=(-b+sqrt(d))/(2*a)
#     x2=(-b-sqrt(d))/(2*a)
    
#     print("the quadratic equation has 2 distinct real roots:",x1,x2)
# else:
#       rp=int(-b/2*a)
#       ip=int(sqrt(abs(d))/(2*a))
#       print(f"the quadratic equation has imaginary roots:{rp} ± i{ip}")
# --------------------------------------------------------------------------------------------
# ArmStrong Numbers Between 0-999
# def counts(i):
#     c=0
#     while i!=0:
#         r=i%10
#         c+=1
#         i=i//10
#     return c
        
# arm=[]
# for i in range(1000):
#     n=i
#     s=0
#     c=counts(i)
#     while n!=0:
#         r=n%10
#         s+=r**c
#         n=n//10
#     if s==i:
#         arm.append(i)
# print(f"there are {len(arm)} armstrong numbers between 0-999:",arm)
# ---------------------------------------------------------------------------------
# a=0
# b=1
# s=0
# fibonacci=[a,b]
# while s<=25:
#     c=a+b
#     a=b
#     b=c
#     fibonacci.append(c)
#     s=c
# print(fibonacci)