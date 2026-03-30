def summaryRanges(nums):
    if not nums:
        return []
    res=[]
    i=0 
    while i<len(nums):
        j=i+1
        while j<len(nums) and nums[j]==nums[j-1]+1:
            j+=1
        if i==j-1:
            res.append(str(nums[i]))
        else:
            res.append(f'{nums[i]}->{nums[j-1]}')
        i=j 
    return res