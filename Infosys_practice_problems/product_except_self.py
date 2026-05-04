'''
✅ Problem: Product of Array Except Self

Question:
Given an array nums, return an array answer such that:

answer[i] = product of all elements except nums[i]
Do NOT use division
Must run in O(n) time
📌 Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]Docstring for Infosys_practice_problems.product_except_self

'''

def productExceptSel(nums):
    n=len(nums)
    if not nums:
        return []
    prefix=1
    ans=[1]*n
    for i in range(n):
        ans[i]=prefix
        prefix*=nums[i]
    suffix=1
    for i in range(n-1,-1,-1):
        ans[i]*=suffix
        suffix*=nums[i]
    return ans 

if __name__=="__main__":
    nums=list(map(int,input().split()))
    res=productExceptSel(nums)
    print(res)