class MergeSorted:
    def mergeSortedArray(self,nums1,m,nums2,n):
        i=0
        j=0 
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                i+=1
            else:
                temp=nums1[i]
                nums1[i]=nums2[j]
                print(nums1)
                i+=1
                nums1[i]=temp
                print(nums1)
                j+=1
        nums1[:]=nums1[:i+1]
        print(nums1)
        nums1.extend(nums2[j:])
        print(nums1)
if __name__=="__main__":
    nums1=[1,2,3,0,0,0]
    nums2=[2,5,6]
    obj=MergeSorted()
    print(obj.mergeSortedArray(nums1,3,nums2,3))