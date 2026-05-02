def maxSumSubArray(arr):
    current_sum=arr[0]
    max_sum=current_sum
    for i in range(1,len(arr)):
        current_sum=max(arr[i],current_sum+arr[i])
        max_sum=max(max_sum,current_sum)
    return max_sum  
def maxSumSubarray_array(arr):
    current_sum=arr[0]
    max_sum=current_sum
    start=end=temp=0
    for i in range(1,len(arr)):
        if arr[i]>current_sum+arr[i]:
            current_sum=arr[i]
            temp=i
        else:
            current_sum+=arr[i]
        if current_sum>max_sum:
            max_sum=current_sum
            start=temp
            end=i
    return arr[start:end+1]

if __name__=="__main__":
    n=int(input("Enter the size of the array: "))
    arr=list(map(int,input().split()))
    result=maxSumSubArray(arr)
    print("The maximum sum of a contiguous subarray is:",result)
    result_array=maxSumSubarray_array(arr)
    print("The contiguous subarray with the maximum sum is:",result_array)
        