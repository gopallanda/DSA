# maximum sum sub array
#Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

# def maxSumCircularSubarray(nums):
#     current_max=max_sum=nums[0]
#     current_min=min_sum=nums[0]
#     total=nums[0]
#     for num in nums[1:]:
#         current_max=max(num,current_max+num)
#         max_sum=max(max_sum,current_max)
#         current_min=min(num,current_min+num)
#         min_sum=min(current_min,min_sum)
#         total+=num
#     return max_sum if max_sum<0 else max(max_sum,total-min_sum)

# if __name__=="__main__":
#     nums = [5,-3,5]
#     max_sum_subArray=maxSumCircularSubarray(nums)
#     print(max_sum_subArray)
    
def twoSum(nums,k):
    temp=sorted(nums)
    l=0
    r=len(nums)-1
    while l<r:
        if temp[l]+temp[r]>k:
            r-=1
        elif temp[l]+temp[r]<k:
            l+=1
        else:
            return list([temp.index(nums[l]),temp.index(nums[r])])
if __name__=="__main__":
    nums = [3,3]
    k=6
    res=twoSum(nums,k)
    print(res)