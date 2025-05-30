def mergeSort(arr):
    n=len(arr)
    if n>1:
        mid=n//2
        left_half=arr[:mid]
        right_half=arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        merge(arr,left_half,right_half)
def merge(arr,left_half,right_half):
    i=j=k=0 
    while i<len(left_half) and j< len(right_half):
        if left_half[i]<right_half[j]:
            arr[k]=left_half[i]
            i+=1
        else:
            arr[k]=right_half[j]
            j+=1
        k+=1
    while  i< len(left_half):
            arr[k]=left_half[i]
            i+=1
            k+=1
    while j< len(right_half):
            arr[k]=right_half[j]
            j+=1
            k+=1
if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    mergeSort(arr)
    print("[" + ','.join(map(str,arr))+"]")