class SortingAlgorithms:
    def BubbleSort(self,arr):
        n=len(arr)
        for i in range(n):
            for j in range(n-i-1):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
    def selectionSort(self,arr):
        n=len(arr)
        for i in range(n):
            min_idx=i
            for j in range(i+1,n):
                if arr[j]<arr[min_idx]:
                    min_idx=j 
            arr[i],arr[min_idx]=arr[min_idx],arr[i]
        return arr  
if __name__=="__main__":
    n=int(input("enter the size of the array:"))
    arr=list(map(int,input("enter the elements of the array:").split()))
    obj=SortingAlgorithms()
    res1=obj.BubbleSort(arr)
    res2=obj.selectionSort(arr)
    print("sorted array using bubble sort is:",res1)
    print("sorted array using selection sort is:",res2)