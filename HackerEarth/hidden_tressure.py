'''

Sample Input
4
51 71 17 42
Sample Output
2
Time Limit: 5
Memory Limit: 256
Source Limit:
Explanation
Given

N = 4, nums = [51, 71, 17, 42]

Approach:

51 → Sum of digits = 6
71 → Sum of digits = 8
17 → Sum of digits = 8
42 → Sum of digits = 6
Valid pairs:

(1,4) → 51 & 42 (sum = 6)
(2,3) → 71 & 17 (sum = 8)
Total = 2

'''

from collections import defaultdict
def solve (n, nums):
    mydict=defaultdict(list)
    res=0
    for num in nums:
        digit_sum=getDigitSum(num)
        mydict[digit_sum].append(num)
    
    for value in mydict.values():
        k = len(value)
        res += k * (k - 1) // 2

    return res
def getDigitSum(num):
    r=0
    total=0
    while num>0:
        r=num%10
        total=total+r
        num=num//10
    return total
if __name__ == "__main__":
    n=int(input())
    nums=list(map(int,input().split()))
    print(solve(n,nums))
    