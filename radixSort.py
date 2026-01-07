def digitSort(arr,exp):
    n=len(arr)
    output=[0]*n
    count=[0]*10
    for num in arr:
        digit=(num//exp)%10
        count[digit]+=1
    for i in range(1,10):
        count[i]+=count[i-1] 
    for i in range(n-1,-1,-1):
        num=arr[i]
        digit=(num//exp)%10
        output[count[digit]-1]=num
        count[digit]-=1
    for i in range(n):  
        arr[i]=output[i]
def radixSort(arr):
    if not arr:
        return arr
    max_val=max(arr)
    exp=1
    while max_val//exp>0:
        digitSort(arr,exp)
        exp*=10
    return arr
if __name__=="__main__":
    n=int(input("enter size of array:"))
    arr=list(map(int,input().split()))
    sorted_arr=radixSort(arr)
    print("sorted array:",sorted_arr)