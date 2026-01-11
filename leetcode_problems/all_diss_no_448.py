def allDisappearNo(arr):
    n=len(arr)
    i=0 
    res=[]
    while i<n :
        correct_index=arr[i]-1
        if 1<=arr[i]<=n and arr[i]!=arr[correct_index]:
            arr[i],arr[correct_index]=arr[correct_index],arr[i]
        else:
            i+=1
    for i in range(n):
        if arr[i]!=i+1:
            res.append(i+1)
    return res
if __name__=="__main__":
    n=int(input("enter size of the array:"))
    arr=list(map(int,input("enter element:").split()))
    res=allDisappearNo(arr)
    print("all disappeared numbers are:",res)
    