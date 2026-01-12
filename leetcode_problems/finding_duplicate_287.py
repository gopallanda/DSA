def findingDuplicate(nums):
    i=0 
    n=len(nums)
    while i<n:
        correct_index=nums[i]-1
        if nums[i]!=nums[correct_index]:
            nums[i],nums[correct_index]=nums[correct_index],nums[i]
        elif i!=correct_index:
            return nums[i]
        i+=1
    return -1
if __name__ == "__main__":
    nums = [3,1,3,4,2]
    print(findingDuplicate(nums))  # Output: 3
    