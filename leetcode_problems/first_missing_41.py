def firstMissingPositive(arr):
    n=len(arr)
    i=0 
    while i <n:
        correct_index=arr[i]-1
        if 1<=arr[i]<=n and arr[i]!=arr[correct_index]:
            arr[i],arr[correct_index]=arr[correct_index],arr[i]
        else:
            i+=1
    for i in range(n):
        if arr[i]!=i+1:
            return i+1
    return n+1
if __name__=="__main__":
    n=int(input("enter size of the array:"))
    arr=list(map(int,input("enter element:").split()))
    res=firstMissingPositive(arr)
    print("first missing positive number is:",res)
    