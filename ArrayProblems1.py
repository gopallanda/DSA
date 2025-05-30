# finding largest element of an array
# def largest(arr):
#     arr.sort()
#     return arr[-1]
# TC= O(nlogn) # sort method take o(nlogn) TC
# approach-2
# def largest(arr):
#     largest=arr[0]
#     for num in arr:
#         if num> largest:
#             largest=num
#     return largest
# arr=[6,3,5,8,7,0]
# print(largest(arr))
# TC= O(logn)
# approach-3
# def largest(arr):
#     return max(arr) # python max has TC= O(logn)
# we can't reduce TC < O(logn)

# find 2nd largest element w/o using sorting

# def secondLargest(arr):
#    if len(arr)<2:
#        return -1
#    largest=float('-inf')
#    sl=float('-inf')
#    for num in arr:
#        if num>largest:
#            sl=largest
#            largest=num
#        elif num>sl and num!=largest:
#            sl=num
#    return sl if sl!=float('-inf') else -1

# arr=[10,0,11,10]
# print(secondLargest(arr))

# left rotate an array by one place
# def LeftRotate(arr):
#     arr[:]=arr[1:]+arr[:1]

#     return arr
# arr=[1,2,3,4,5]
# print("array before rotation:",arr)
# LeftRotate(arr)
# print("array after rotation:",arr)


# Difference Between arr and arr[:]
# arr = arr[1:] + arr[:1] (Not modifying original)

# Here, arr[1:] + arr[:1] creates a new list.
# When you assign arr = new_list, arr now refers to a completely new object.
# The original arr outside the function remains unchanged because arr inside the function is just a local variable.
# arr[:] = arr[1:] + arr[:1] (Modifying in place)

# arr[:] means "modify the entire contents of the list in place".
# It does not create a new list but rather modifies the existing list element by element.
# Since arr[:] refers to the original list, changes are reflected outside the function.


# moving all zeroes to end
# not in-place 
# def moveZeroes( nums):
#         j=len(nums)-1
#         i=0
#         while i<j:
#             if nums[j]==0:
#                 j-=1
#             elif nums[i]==0:
#                 nums[i],nums[j]=nums[j],nums[i]
#             else:
#                 i+=1
#         return arr
# arr=[0,1,0,3,12]
# print(moveZeroes(arr)) # [12, 1, 3, 0, 0] not in-place
# # in-place 
# def move_Zeroes(nums):
#     n = len(nums)
#     pos = 0  # Pointer to track non-zero elements

#     # Move non-zero elements to the front
#     for i in range(n):
#         if nums[i] != 0:
#             nums[pos] = nums[i]
#             pos += 1
    
#     # Fill the rest with zeroes
#     for i in range(pos, n):
#         nums[i] = 0

#     return arr
# arr=[0,1,0,3,12]
# print(move_Zeroes(arr)) # [1, 3, 12, 0, 0]

# def findUnion(a,b):
#         # code here 
#         for i in a:
#             for j in b:
#                 if j not in a:
#                     a.append(j)
#         a.sort()
#         return a
# a= [1, 2, 3, 4, 5]
# b=[1, 2, 3, 6, 7]
# print(findUnion(a,b))
# but it will not consider the situation where a has duplicate elements
# def findUnion(a,b):
#     temp=set(a+b)
#     res=sorted(temp)
#     return res
# a=[2,3,3,4,5,6,6]
# b=[4,5,6,7]
# print(findUnion(a,b))

# maximum consecutive 1's

# def findConsecutiveOnes(arr):
#     max_count=0
#     count=0
#     for i in range(len(arr)):
#         if arr[i]==1:
#             count+=1
#             if max_count<count:
#                 max_count=count
#         else:
#             count=0
#     return max_count
# arr=[1,1,0,1,1,1] # 3
# print(findConsecutiveOnes(arr))
# time complexity O(n)

# Given an array arr[] containing integers and an integer k, your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. If there is no subarray with sum equal to k, return 0.

# Examples:

# Input: arr[] = [10, 5, 2, 7, 1, -10], k = 15
# Output: 6
# Explanation: Subarrays with sum = 15 are [5, 2, 7, 1], [10, 5] and [10, 5, 2, 7, 1, -10]. The length of the longest subarray with a sum of 15 is 6.

# def longest_subarray_with_sum_k(arr, k):
#     prefix_sum = {}
#     current_sum = 0
#     max_length = 0
    
#     # Initialize with 0 sum at index -1 to handle exact match
#     prefix_sum[0] = -1

#     for i in range(len(arr)):
#         current_sum += arr[i]
        
#         # Check if current_sum - k exists
#         if (current_sum - k) in prefix_sum:
#             max_length = max(max_length, i - prefix_sum[current_sum - k])

#         # Store current_sum if not already present
#         if current_sum not in prefix_sum:
#             prefix_sum[current_sum] = i

#     return max_length

# # Example
# print(longest_subarray_with_sum_k([10, 5, 2, 7, 1, -10], 15))  # Output: 6
