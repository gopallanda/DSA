# 1) Input: n = 10
#    Output: 1 2 3 4 5 6 7 8 9 10

# def Series(n):
#     if n==1:
#         print(1,end=" ")
#         return
#     else:
#         Series(n-1)
#     print(n,end=" ")
# n=int(input("enter no of terms:"))
# Series(n)

# 2) to reverse above series 10 9 8 7 6 5 4 3 2 1 
# def Series(n):
#     if n==1:
#         print(1,end=" ")
#         return
#     print(n,end=" ")
#     Series(n-1)
    
# n=int(input("enter no of terms:"))
# Series(n)

# 3) print a string no of times
# def printString(n,string):
#         # Code here
#         if n==1:
#             print(string,end=" ")
#             return
#         else:
#               printString(n-1,string)
#         print(string,end=" ")
# string=input("enter a string:")
# n=int(input("enter no of times to be repeat:"))
# printString(n,string)

# enter a string:smile😊
# enter no of times to be repeat:5
# smile😊 smile😊 smile😊 smile😊 smile😊 

# 4) Input: n = 5
#    Output: 225
#    Explanation: 13 + 23 + 33 + 43 + 53 = 225
# def sumOfSeries(n):
#         #code here
#         if n==0:
#             return 0
#         if n==1:
#            return 1**3
#         return n**3+sumOfSeries(n-1)
# n=int(input("enter no of terms:"))
# x=sumOfSeries(n)
# print(x)
    

