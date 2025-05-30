def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        j=i-1
        key_element=arr[i]
        while j>=0 and arr[j]>key_element:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key_element
if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    insertionSort(arr)
    print("["+','.join(map(str,arr))+"]")
