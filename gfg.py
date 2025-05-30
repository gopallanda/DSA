# def sort_by_binary_ones_desc(arr):
#     # Sort by the count of '1's in binary representation in descending order.
#     # If there's a tie, sort by the number itself in ascending order.
#     return sorted(arr, key=lambda x: (-bin(x).count('1'), x))

# # Example usage
# arr = [3, 7, 8, 9, 1, 2]
# sorted_arr = sort_by_binary_ones_desc(arr)
# print(sorted_arr)


# arr=[1,2,-3,4,5]
# k=1
# #arr.sort()
# while k>0:
#     i=arr.index(min(arr))
#     arr[i]=-arr[i]
#     print(arr)
#     k-=1
# print(sum(arr))
# arr = [1, 2, 3, 4, 5]
# l = len(arr)
# i = 0
# j = l - 1

# while i < j:
#     arr[i], arr[j] = arr[j], arr[i]
#     i += 1
#     j -= 1

# print(arr)
# arr=[2,1,5,5,5,5,6,6,6,6]
# l=len(arr)
# res=[]
# for i in set(arr):
#     c=arr.count(i)
#     if c>l/3:
#         res.append(i)
# print(res)
# from collections import deque

# arr=[8, -8, 9, -9, 10, -11, 12]
# dq=deque(arr)

# sums=0
# for i in range(len(arr)):
#     dq.rotate(1)
#     if sums<sum(dq):
#         sums=sum(dq)
# print(dq)
# print(sums)

# arr= [-8, 0, -1, -4, -3] 
# arr.sort()
# print(arr)
# for i in range(len(arr)):
#     if arr[i]>=0:
#         if arr[i]+1 not in arr:
#             print(arr[i]+1)
#             break
            
# s1='act'
# s2='tact'
# for char in s1:
#     if char in s2:
#         pos=True
#     else:
#         pos=True
# print(sorted(s1))
# print(sorted(s2))

# print(sorted(s1)==sorted(s2))
# l1=[1,2,3,4]
# l2=[4,2,3,1]
# print(l1==sorted(l2))
# s='racecar'
# c=[]
# for i in s:
#     if s.count(i)>1:
#         pass
#     else:
#         c.append(i)
#         break
# if len(c)==0:
#     print("false")
# else:
#     print(c[0])
# name=[1,2,3]
# c=(name[::-1])
# print(c)
# a= [2, 4, 7, 10]
# b= [2, 3]
# c=a+b
# print(c)
# a.extend(b)
# a.sort()
# b=a[len(a)-len(b):]
# a=a[0:len(a)-len(b)]
# print(a)
# print(b)

# def mergeArrays(a, b):
#         # code here
#         a.extend(b)
#         a.sort()
#         b=a[len(a)-len(b):]
#         a=a[0:len(a)-len(b)]
#         return a,b
# res=mergeArrays([2,4,7,8],[2,3])
# print(res)
# arr=[1,2,2,3,3,4,5,6,7,8]
# print(arr.count(22))
# a=[2, 3, 6, 7, 9]
# b=[1, 4, 8, 10]
# a.extend(b)
# print(a)
# a.sort()
# print(a)
# # print(a[4])
# list1=[2,3,4,7,11]
# miss=[]
# k=1
# while k!=list[0]:
#     miss.append(k)
#     k+=1
# for i in range(len(list1)):
#     k=list[i]
#     while k!=list1[i+1]:
#         if k in list1:
#             k+=1
#         else:
#             miss.append(k)
#             k+=1



# arr=[2, 3, 2, 3, 5]
# freq={}
# for i in arr:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(list(freq.values()))

