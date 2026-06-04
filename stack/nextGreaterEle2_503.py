''' next greater element II is similar to next greater element I but in this problem we are given a circular array. We can solve this problem using a stack. We will iterate through the array twice and for each element we will check if it is greater than the top element of the stack. If it is greater than the top element of the stack we will pop the top element from the stack and update the result for that element. We will continue this process until we find an element that is greater than the top element of the stack or until the stack is empty. Finally, we will return the result array. example input: [1,2,1] output: [2,-1,2]
'''
def nextGreaterElements(nums):
    n=len(nums)
    res=[-1]*n
    stack=[]
    for i in range(2*n):
        while stack and nums[stack[-1]]<nums[i%n]:
            small=stack.pop()
            res[small]=nums[i%n]
        stack.append(i%n)
    return res
if __name__=="__main__":
    nums=list(map(int,input().split()))
    result=nextGreaterElements(nums)
    print(result)