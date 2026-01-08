def moveZeroes(arr):
    pos=0 
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[pos]=arr[i]
            pos+=1
    for i in range(pos,len(arr)):
        arr[i]=0
    return arr
if __name__=="__main__":
    n=int(input("size of array:"))
    arr=list(map(int,input("enter the elements:").split()))
    res=moveZeroes(arr)
    print("Array after moving zeroes to the end:",res)