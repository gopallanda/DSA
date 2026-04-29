def binarySubArrays(nums,goal):
    def atMost(goal):
        if goal<0:
            return 0
        left=0
        res=0
        current_sum=0
        for right in range(len(nums)):
            current_sum+=nums[right]
            while current_sum>goal:
                current_sum-=nums[left]
                left+=1
            res+=right-left+1
        return res 
    return atMost(goal)-atMost(goal-1)
if __name__=='__main__':
    nums=[1,0,1,0,1]
    goal=2
    print(binarySubArrays(nums,goal))  # Output: 4