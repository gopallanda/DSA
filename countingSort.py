def countingSort(arr):
    if not arr:
        return arr 
    max_val=max(arr)
    count=[0]*(max_val+1)
    for num in arr:
        count[num]+=1
    for i in range(1, len(count)):
        count[i]+=count[i-1]
    res=[0]*len(arr)
    for i in range(len(arr)-1,-1,-1):
        num=arr[i]
        res[count[num]-1]=num 
        count[num]-=1 
    return res
if __name__=="__main__":
    n=int(input("enter size of array:"))
    arr=list(map(int,input().split()))
    sorted_arr=countingSort(arr)
    print("sorted array:",sorted_arr)