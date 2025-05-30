class Solution:
    def smallestSubWithSum(self, x, arr):
        a=[]
        sum=0
        while sum>x:
            n=max(arr)
            a.append(n)
            arr.remove(n)
        return len(a)    



#{ 
 # Driver Code Starts
def main():

    T = int(input())

    while (T > 0):
        x = int(input())
        a = [int(x) for x in input().strip().split()]
        print(Solution().smallestSubWithSum(x, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends