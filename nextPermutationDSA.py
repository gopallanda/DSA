def nextPermutation(arr):
    n=len(arr)
    i=n-2
    while i>=0 and arr[i]>=arr[i+1]:
        i-=1
    if i>=0:
        j=n-2
        while arr[j]<=arr[i]:
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
    arr[i+1:]=sorted(arr[i+1:])
    return arr
n=int(input("enter the size of the array:"))
arr=[]
for i in range(n):
    arr.append(int(input(f"enter the element of the index{i}:")))
k=nextPermutation(arr)
print("next permutation of the array:",k)
