'''
DocProblem: Subarray Sum Equals K

Question:
Given an array nums and an integer k, return the total number of subarrays whose sum equals k.

📌 Example:
Input: nums = [1,1,1], k = 2
Output: 2 
'''


def subArraySumEqualsK(nums,k):
    count=0 
    l=0
    curr_sum=0
    for r in range(len(nums)):
        curr_sum+=nums[r]
        if curr_sum==k:
            count+=1
        while curr_sum>k:
            curr_sum-=nums[l]
            l+=1
            if curr_sum==k:
             count+=1
    return count
if __name__=="__main__":
    nums=list(map(int,input("Enter the array elements: ").split()))
    k=int(input("Enter the value of k: "))
    res=subArraySumEqualsK(nums,k)
    print(res)
    
# the above code is not working for all test cases, it is only working for positive numbers, we need to use a hashmap to store the cumulative sum and its frequency to handle negative numbers as well. Here is the corrected code:

# PREFIX SUM + HASHMAP APPROACH

def subArraySumEqualsToK(nums,k):
    count=0 
    prefix_sum=0
    prefix_map={0:1}
    for num in nums:
        prefix_sum+num
        if prefix_sum-k in prefix_map:
            count+=prefix_map[prefix_sum-k]
        prefix_map[prefix_sum]=prefix_map.get(prefix_sum,0)+1
    return count
