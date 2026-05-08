'''Problem: Find All Anagrams in a String

Question:
Given two strings s and p, return all start indices of p’s anagrams in s.

📌 Example:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
'''

from collections import Counter
def findAllAnagrams(s,p):
    if len(p)>len(s):
        return []
    k=len(p)
    p_count=Counter(p)
    s_count=Counter(s[:k])
    result=[]
    for i in range(k,len(s)):
        if s_count==p_count:
            result.append(i-k)
        s_count[s[i]]+=1
        s_count[s[i-k]]-=1
        if s_count[s[i-k]]==0:
            del s_count[s[i-k]]
    if s_count==p_count:
        result.append(len(s)-k)
    return result

if __name__=="__main__":
    s=input("Enter the string s: ")
    p=input("Enter the string p: ")
    result=findAllAnagrams(s,p)
    print(result)
        
        
        
    
    
    