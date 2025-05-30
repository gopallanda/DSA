# 2sum problem return yes/no or indices

# def twoSum(arr,k):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n):
#             if arr[i]+arr[j]==k:
#                 return "Yes"
#     return "No"
# arr=[2,6,5,8,11]
# target=14
#print(twoSum(arr,target))

# def twoSum(arr,k):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n):
#             if arr[i]+arr[j]==k:
#                 return list([i,j])
#     return list([-1,-1])
# arr=[2,6,5,8,11]
# target=14
# print(twoSum(arr,target))

#better approach using hashmap
# def twoSum(arr,k):
#     n=len(arr)
#     h_m={}
#     for i in range(n):
#         if k-arr[i] in h_m:
#             h_m[k-arr[i]]=i
#             return "yes"
#         else:
#             h_m[arr[i]]=i
#     return "NO"
        
# arr=[2,6,5,8,11]
# target=14
# print(twoSum(arr,target))

# def twoSum(arr,k):
#     n=len(arr)
#     h_m={}
#     for i in range(n):
#         if k-arr[i] in h_m:
            
#             return list([i,h_m[k-arr[i]]])
#         else:
#             h_m[arr[i]]=i
#     return list([-1,-1])
        
# arr=[2,6,5,8,11]
# target=14
# print(twoSum(arr,target))

#using 2 pointer approach



# def twoSum(nums,target):
       
#         nums =sorted((num, i) for i, num in enumerate(nums))  # Sort with indices
#         print(nums)
#         left, right = 0, len(nums) - 1
        
#         while left < right:
#             if nums[left][0] + nums[right][0] == target:
#                 return [nums[left][1], nums[right][1]]  # Return original indices
#             elif nums[left][0] + nums[right][0] < target:
#                 left += 1
#             else:
#                 right -= 1

#         return [-1, -1]  # No solution found 
# arr=[2,6,5,8,11]
# target=14
# print(twoSum(arr,target))

# The enumerate() function iterates over a tuple or list and returns an enumerate object, which yields tuples containing the index and the corresponding element.


# sorting 0's, 1's, 2's

# # Brute force approach

# def sortNums(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(n):
#             if arr[i]<arr[j]:
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr
# nums = [2,0,2,1,1,0]
# print(sortNums(nums))
# TC= O(n)^2

# Better approach counting Sort approach

# def sortNums(arr):
#     count0=0
#     c0=0
#     c1=0 
#     c2=0 
#     for num in arr:
#         if num==0:
#             c0+=1
#         elif num==1:
#             c1+=1
#         else:
#             c2+=1
#     for i in range(c0):
#         arr[i]=0
#     for i in range(c0,c0+c1):
#         arr[i]=1
#     for i in range(c0+c1,c0+c1+c2):
#         arr[i]=2
#     return arr
# nums = [2,0,2,1,1,0]
# print(sortNums(nums))
# although there are 4 for loops but each loop execute at a time only b?c they are not nested
# TC= O(n)

# optimal approach

#Dutch National Flag Algorithm (Three Pointers)

# def sortNums(arr):
#     low,mid,high=0,0,len(arr)-1
#     while mid<=high:
#         if arr[mid]==0:
#             arr[low],arr[mid]=arr[mid],arr[low]
#             mid+=1
#             low+=1
#         elif arr[mid]==1:
#             mid+=1
#         else:
#             arr[mid],arr[high]=arr[high],arr[mid]
#             high-=1
#     return arr 
# nums = [2,0,2,1,1,0]
# print(sortNums(nums))

# TC= O(n)
# although counting sort and dutch national flag problem has O(n) TC
# but the advantages of this algo are
# => no of pases 1 in Dutch where as 2 in counting.. 
# => in place without over writing 
# 💡 In-place means:
# You modify the original array without using extra memory (like another array or list). You’re reusing the existing space.

# 🖊️ Overwriting means:
# You replace the current values in the array with new ones, usually based on counting or logic — like setting arr[i] = 0, arr[i] = 1, etc.

# 📌 So, what does "in-place without overwriting" mean?
# It means:

# You rearrange or sort the elements only by swapping, not by resetting their values manually.

# You do not destroy or overwrite values with constants like 0, 1, or 2. You let the array "reorganize itself."

# majority element
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# brute force method
# def longest(arr):
#     count=0 
#     n=len(arr)
#     max_count=n//2
#     n=len(arr)
#     for i in arr:
#         if arr.count(i)>max_count:
#             max_count=arr.count(i)
#             max_value=i
#     return max_value
# nums = [2,2,1,1,1,2,2]
# print(longest(nums)) # 2


#Boyer-Moore Majority Voting Algorithm
# in this algorithm we find the potential element that can be a majority element
# but it is always not true that why we check for the count_element>n/2
# it contains 2 loops 1 for find potential element
# 2 to validate the occurance

# def longest(arr):
#     ele=0
#     count=0 
#     n=len(arr)
#     for i in range(n):
#         if count==0:
#             count=1 
#             ele=arr[i]
#         elif ele==arr[i]:
#             count+=1 
#         else:
#             count-=1 
#     for i in range(n):
#         if arr[i]==ele :
#             count+=1 
#     if count>n/2:
#         return ele 
#     else:
#         return -1
        
# nums = [2,2,1,1,1,2,2]
# print(longest(nums)) # 2
    
#set matrix elements to 0 if any row/col contains 0
# def setZeroes(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
#     first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))
#     print(first_row_has_zero)
#     print(first_col_has_zero)
#     # Use first row and first column as markers
#     for i in range(1, m):
#         for j in range(1, n):
#             if matrix[i][j] == 0:
#                 matrix[i][0] = 0  # mark the row
#                 matrix[0][j] = 0  # mark the column
#     # Zero out cells based on markers
#     for i in range(1, m):
#         for j in range(1, n):
#             if matrix[i][0] == 0 or matrix[0][j] == 0:
#                 matrix[i][j] = 0
#     # Zero out first row if needed
#     if first_row_has_zero:
#         for j in range(n):
#             matrix[0][j] = 0
#     # Zero out first column if needed
#     if first_col_has_zero:
#         for i in range(m):
#             matrix[i][0] = 0
#     return matrix
# if __name__=='__main__':
#     arr=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
#     res=setZeroes(arr)
#     print(res)

# rotate an array by 90 deg
# to rotate 90 deg first we transpose the matrix
# then reverse the each row
# def rotateArray(matrix):
#     n=len(matrix)
#     for i in range(n):
#         for j in range(i+1,n):
#             matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
#     for i in range(n):
#         matrix[i].reverse()
#     return matrix
# if __name__=='__main__':
#     matrix=[ [5,1,9,11],
#              [2,4,8,10],
#              [13,3,6,7],
#              [15,14,12,16]
#            ]            
#     res=rotateArray(matrix)
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             print(res[i][j],end=" ")
#         print()
# 5 13 2 5 
# 14 3 4 1 
# 12 6 8 9 
# 16 7 10 11

# Subarray Sum Equals K
def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0
    freq = {0: 1}  # To count subarrays starting from index 0

    for num in nums:
        prefix_sum += num
        count += freq.get(prefix_sum - k, 0)
        freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

    return count
    
if __name__=="__main__":
    nums = [1,1,1]
    k = 2
    res=subArraySum(nums,k)
    print(res)
               