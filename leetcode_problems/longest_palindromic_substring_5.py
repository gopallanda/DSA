def longestPalindromicSubstring(s):
    if not s:
        return ""
    def partitionAroundCentre(l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
    res=''
    for i in range(len(s)):
        odd=partitionAroundCentre(i,i)
        even=partitionAroundCentre(i,i+1)
        res=max(res,odd,even,key=len)
    return res   
if __name__ == "__main__":
    s="babad"
    print(longestPalindromicSubstring(s))  # Output: "bab" or "aba"