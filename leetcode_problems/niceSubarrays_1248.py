def niceSubarrays(nums,k):
  def max_count(k):
    left=0
    odd_count=0
    res=0  
    for right in range(len(nums)):
        if nums[right] % 2 == 1:
            odd_count += 1
        while odd_count > k:
            if nums[left] % 2 == 1:
                odd_count -= 1
            left += 1
        res += right - left + 1
    return res 
  return max_count(k) - max_count(k - 1)

if __name__=='__main__':
    nums=[1,1,2,1,1]
    k=3
    print(niceSubarrays(nums,k))  # Output: 2