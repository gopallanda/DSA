# power set using iterative approach
# class PowerSet:
#     def powerset(self,nums):
#         ps=[[]]
#         for num in nums:
#             current_set=[current+[num] for current in ps]
#             ps.extend(current_set)
#         return ps
# if __name__=="__main__":
#         ps=PowerSet()
#         nums=list(map(int,input().split()))
#         obj=PowerSet()
#         result=obj.powerset(nums)
#         print(result)
#         print("Total subsets:", len(result))
#         print("Total elements in the original set:", len(nums))    
       
# power set using back tracking approach
class PowerSet:
    def __init__(self):
        self.res=[]
    def backTrack(self,start,path,nums):
        self.res.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            self.backTrack(i+1,path,nums)
            path.pop()
    def generateSubsets(self,nums):
        self.backTrack(0,[],nums)
        return self.res
if __name__=="__main__":
    nums=list(map(int,input().split()))
    ps=PowerSet()
    result=ps.generateSubsets(nums)
    print(result)
