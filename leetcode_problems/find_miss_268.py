def findMissing(arr):
    n=len(arr)
    i=0 
    while i<n:
        correct_index=arr[i]
        if arr[i]<n and arr[i]!=arr[correct_index]:
            arr[i],arr[correct_index]=arr[correct_index],arr[i]
        else:
            i+=1
    for i in range(n):
        if arr[i]!=i:
            return i    
    return n  
if __name__=="__main__":
    n=int(input("enter size of the array:"))
    arr=list(map(int,input("enter element:").split()))
    res=findMissing(arr)
    print("missing number is:",res)