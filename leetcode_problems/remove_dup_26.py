def removeDup(arr):
    if not arr:
        return 0 
    i=0
    for j in range(1,len(arr)):
        if arr[j]!=arr[i]:
            i+=1
            arr[i]=arr[j]
    return i+1 
if __name__=="__main__":
    n=int(input("size of array:"))
    arr=list(map(int,input("enter the elements:").split()))
    length=removeDup(arr)
    print("Array after removing duplicates:",arr[:length])
        