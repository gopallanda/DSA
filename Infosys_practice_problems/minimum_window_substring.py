'''
Minimum Window Substring

Question:
Given strings s and t, return the minimum window substring of s such that every character in t is included in the window.

If no such window exists, return "".

📌 Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC" 
'''

from collections import Counter
def minimumWindowSubstring(s,t):
    need=Counter(t)
    have=Counter()
    required=len(need)
    formed=0
    left=0
    ans=(float("inf"),0,0)
    for right,ch in enumerate(s):
        have[ch]+=1
        if ch in need and have[ch]==need[ch]:
            formed+=1
        while formed==required:
            if right-left+1<ans[0]:
                ans=(right-left+1,left,right)
            have[s[left]]-=1 
            if s[left] in need and have[s[left]]<need[s[left]]:
                formed-=1 
            left+=1 
    return "" if ans[0]==float("inf") else s[ans[1]:ans[2]+1]
if __name__=="__main__":
    s=input()
    t=input()
    result=minimumWindowSubstring(s,t)
    print(result)
    