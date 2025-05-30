Input: arr[] = [2, 3, 2, 3, 5]
Output: [0, 2, 2, 0, 1]
Explanation: We have: 1 occurring 0 times, 2 occurring 2 times, 3 occurring 2 times, 4 occurring 0 times, and 5 occurring 1 time.


reversing an array
def frequencyCount(self, arr):
        #  code here
      max_val = len(arr)  # Find the maximum element
      freq = [0] * (max_val + 1)  # Create a frequency array

    # Count occurrences of each element
      for num in arr:
        freq[num] += 1

      return freq[1:] 
def reverseArray( arr):
        def help(start,end):
          if start>=end:
            return
          arr[start],arr[end]=arr[end],arr[start]
          help(start+1,end-1)
        help(0,len(arr)-1)
        return arr
arr=[1,2,3,4]
print(reverseArray(arr))


class recursion:
    def reverseArray(self,arr,start,end):
      if start>=end:
        return
      arr[start],arr[end]=arr[end],arr[start]
      self.reverseArray(arr,start+1,end-1)
      return arr
obj=recursion()
arr=[1,2,3,4]
x=obj.reverseArray(arr,0,len(arr)-1)
print(x)

class Solution:
    def reverseArray(self,arr,start=0,end=len(arr)-1):
        if start>=end:
            return
        arr[start],arr[end]=arr[end],arr[start]
        self.reverseArray(arr,start+1,end-1)
        return arr
this code will throw name error as arr not defined 
reason
In Python, default arguments are evaluated only once when the function is defined, not each time the function is called.

corrected code
class Solution:
    def reverseArray(self,arr,start=0,end=None):
        if end==None:
            end=len(arr)-1
        if start>=end:
            return
        arr[start],arr[end]=arr[end],arr[start]
        self.reverseArray(arr,start+1,end-1)
        return arr
        
check palindrome using recursion
class Base:
    def isPalindrome(self,s,start=0,end=None):
        s = ''.join(c.lower() for c in s if c.isalnum())
        # this is used to handle special characters
        #eg: "A man, a plan, a canal: Panama"
        if end==None:
            end=len(s)-1
        if start<=end:
            if s[start]==s[end]:
                start+=1
                end-=1
                return self.isPalindrome(s,start,end)
            else:
                return False
        else:
            return True
string=input("enter a name:")
obj=Base()
print(obj.isPalindrome(string))

# optimized code by reducing space complexity 
class Solution:
    def isPalindrome(self, s: str, start=0, end=None) -> bool:
        if end is None:
            end = len(s) - 1  # Initialize end pointer

        # Move start forward if not alphanumeric
        while start < end and not s[start].isalnum():
            start += 1
        # Move end backward if not alphanumeric
        while start < end and not s[end].isalnum():
            end -= 1

        # Base case: If start crosses end, it's a palindrome
        if start >= end:
            return True

        # Compare characters (ignoring case)
        if s[start].lower() != s[end].lower():
            return False

        # Recursive call with updated pointers
        return self.isPalindrome(s, start + 1, end - 1)

# this how space complexity is reduced 
# s = ''.join(c.lower() for c in s if c.isalnum()) creates a new string of length O(n) in the worst case.
This extra string requires O(n) space.

fibonacci using recursion
class Base:
    
    def fibonacci(self,n):
        if n==0:
            return 0
        elif n==1:
            return 0
        elif n==2:
            return 1
            
            
        else:
            return self.fibonacci(n-1)+self.fibonacci(n-2)
n=int(input("enter range:"))
obj=Base()
x=obj.fibonacci(n)
print(f"sum of {n} fibonacci numbers is {x}")