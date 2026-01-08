def threeSum(arr):
    arr.sort()
    res=[]
    for i in range(len(arr)-2):
        if i>0 and arr[i]==arr[i-1]:
            continue
        left=i+1
        right=len(arr)-1
        while left<right:
            total=arr[i]+arr[left]+arr[right]
            if total<0:
                left+=1
            elif total>0:
                right-=1
            else:
                res.append([arr[i],arr[left],arr[right]])
                while left<right and arr[left]==arr[left+1]:
                    left+=1
                while left<right and arr[right]==arr[right-1]:
                    right-=1
                left+=1
                right-=1
        return res
if __name__=="__main__":
    n=int(input("size of array:"))
    arr=list(map(int,input("enter the elements:").split()))
    result=threeSum(arr)
    print("Unique triplets that sum to zero are:",result)