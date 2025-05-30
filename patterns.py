# *****
# *****
# *****
# *****
# *****
# r=5
# c=5
# for i in range(r):
#     print('*'*c)

# *
# **
# ***
# ****
# *****

# r=5
# for i in range(1,r+1):
#     print('*'*i)

# r=5
# i=1
# while i<=r:
#     print('*'*i)
#     i+=1

# for i in range(3):
#     for j in range(4):
#         print("*",end=" ")
#     print()

#     *    
#    ***   
#   *****
#  *******
# *********

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end='')
#     for j in range(n-i-1):
#         print(" ",end="")
#     print()


# *********
#  ******* 
#   *****
#    ***
#     *


# n=5
# for i in range(n):
#     for j in range(i):
#         print(" ",end='')
#     for k in range(2*n-(2*i+1)):
#         print("*",end='')
#     for j in range(i):
#         print(" ",end='')
#     print()


#     *    
#    ***   
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
 

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end='')
#     for j in range(n-i-1):
#         print(" ",end="")
#     print()
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n*2-(2*i+1)):
#         print("*",end='')
#     for j in range(i):
#         print(" ",end="")
#     print()
    
# * 
# ** 
# ***
# ****
# *****
# ****
# ***
# **
# *


# n=5  
# for i in range(n):
#    print('*'* (i+1),end=" ")
#    print()
# for j in range(n-1):
#     print('*'*(n-1-j),end=' ')
#     print()


# tricky problem 1😎

# 1 
# 0 1 
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1


# n=5  
# for i in range(n):
#    if i%2==0:
#       start=1
#    else:
#       start=0
#    for j in range(n):
#       if j<=i:
#          if start==0:
#             print(start,end=" ")
#             start=1 
#          else:
#             print(start,end=" ")
#             start=0
#    print()

# 1                 1 
# 1 2             2 1 
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1

# n=5 
# for i in range(n):
#    for j in range(n):
#       if j<=i:
#          print(j+1,end=" ")
#          k=j
      
#       else:
#          print(" ",end=" ")
#    for j in range(n):
#       if j>=n-i-1:
         
#          print(n-j,end=" ")
         
#       else:
#          print(" ",end=' ')
#    print()


# 1 
# 2 3 
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# n=5
# k=0
# for i in range(n):
#    for j in range(n):
#       if j<=i:
#          print(k+1,end=" ")
#          k+=1
#    print()

# A 
# A B 
# A B C
# A B C D
# A B C D E

# n=5 
# for i in range(n):
#    ch='A'
#    for j in range(n):
#       if j<=i:
#          print(ch,end=" ")
#          ch=chr(ord(ch)+1)
#    print()

# A B C D E
# A B C D
# A B C
# A B
# A
# for i in range(n):
#      ch="A"
#      for j in range(n-i):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#      print()

# A 
# B B
# C C C
# D D D D
# E E E E E

# n=5 
# ch="A"
# for i in range(n):
#    for j in range(n):
#       if j<=i:
#          print(ch,end=" ")
#    print()
#    ch=chr(ord(ch)+1)

# n=5
# for i in range(n):
#     ch = "A"
#     for j in range(n - i - 1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print(ch, end="")
#         ch = chr(ord(ch) + 1)
#     ch = chr(ord(ch) - 2)
#     for l in range(i):
#         print(ch, end="")
#         ch = chr(ord(ch) - 1)
#     print()

#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA