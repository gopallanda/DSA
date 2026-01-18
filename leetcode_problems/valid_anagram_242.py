def validAnagram(s,t):
    if len(s)!=len(t):
        return False
    for char in t:
        if char in s and s.count(char)==t.count(char):
            continue
        else:
            return False 
    return True 
if __name__ == "__main__":
    s="anagram"
    t="nagaram" 
    print(validAnagram(s,t))  # Output: True