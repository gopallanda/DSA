def max_subArray(nums,k):
    n=len(nums)
    curr_sum=sum(nums[:k])
    max_sum=curr_sum
    for i in range(k,n):
        curr_sum+=nums[i]-nums[i-k]    
        max_sum=max(max_sum,curr_sum)
    return max_sum/k
if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    print(max_subArray(nums,k))  # Output: 12.75