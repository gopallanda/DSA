'''
DocNextGreater element is a leetcode problem 496: Next Greater Element I , the problem is to find the next greater element for each element in nums1 from nums2. The next greater element of a number x in nums2 is the first greater number to the right of x in nums2. If it does not exist, return -1 for this number. example input: nums1 = [4,1,2], nums2 = [1,3,4,2] output: [-1,3,-1] explanation: For number 4 in nums1, there is no greater number to its right in nums2, so the output is -1. For number 1 in nums1, the next greater number to its right in nums2 is 3. For number 2 in nums1, there is no greater number to its right in nums2, so the output is -1. The solution uses a stack to keep track of the elements in nums2 and a dictionary to store the next greater element for each number. The algorithm iterates through nums2, and for each number, it pops elements from the stack until it finds a greater number. The popped elements are then mapped to the current number in the dictionary. Finally, the algorithm constructs the
'''


def nextGreaterElement(nums1,nums2):
    stack=[]
    next_greater={}
    for num in nums2:
        while stack and stack[-1]<num:
            small=stack.pop()
            next_greater[small]=num
        stack.append(num)
    res=[next_greater.get(num,-1) for num in nums1]
    return res
if __name__=="__main__":
    nums1=list(map(int,input("Enter the elements of nums1: ").split()))
    nums2=list(map(int,input("Enter the elements of nums2: ").split()))
    result=nextGreaterElement(nums1,nums2)
    print("The next greater elements for nums1 in nums2 are:", result)