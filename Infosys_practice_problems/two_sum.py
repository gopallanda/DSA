'''
DocProblem: Two Sum II - Input Array Is Sorted

Question:
Given a sorted array of integers numbers and an integer target, return the indices (1-based) of the two numbers such that they add up to target.

You must use O(1) extra space.

📌 Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]string for Infosys_practice_problems.two_sum
'''

def twoSum(nums,target):
    n=len(nums)
    left=0
    right=n-1
    while left<right:
        current_sum=nums[left]+nums[right]
        if current_sum==target:
            return [left+1,right+1]
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return []

if __name__=="__main__":
    numbers= list(map(int,input().split()))
    target=int(input())
    result=twoSum(numbers,target)
    print(result)
    