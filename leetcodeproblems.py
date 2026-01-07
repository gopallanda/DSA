#3 sum problem:
def ThreeSum(nums):
    nums.sort()
    res=[]
    for i in range(len(nums)-2): 
        if i>0 and nums[i]==nums[i-1]:
            continue
        left=i+1
        right=len(nums)-1
        while left<right:
            total=nums[i]+nums[left]+nums[right]
            if total<0:
                left+=1
            elif total>0:
                right-=1
            else:
                res.append([nums[i],nums[left],nums[right]])
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right+1]:
                    right-=1
            left+=1
            right-=1
    return res 
if __name__=="__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    res=ThreeSum(nums)
    print(res)