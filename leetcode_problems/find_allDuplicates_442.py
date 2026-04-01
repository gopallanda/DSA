def findAllDuplicates(nums):
    i=0 
    n=len(nums)
    res=[]
    while i<n:
        correct_index=nums[i]-1
        if nums[i]!=nums[correct_index]:
            nums[i],nums[correct_index]=nums[correct_index],nums[i]
        else:
            i+=1
    for i in range(n):
        if nums[i]!=i+1:
            res.append(nums[i])
    return res 