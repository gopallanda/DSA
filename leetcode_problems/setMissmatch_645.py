def setMissMatch(nums):
    i=0 
    n=len(nums)
    res=[]
    while i<n:
        correct_index=nums[i]-1
        if nums[i]!=nums[correct_index]:
            nums[i],nums[correct_index]=nums[correct_index],nums[i]
        else:
            i+=1
    print(nums)
    for i in range(n):
        if nums[i]!=i+1:
            res.append(nums[i])
            res.append(i+1)
    print(res)
    
    
if __name__=="__main__":
    n=int(input("enter size of the array:"))
    arr=list(map(int,input().split()))
    setMissMatch(arr)
    