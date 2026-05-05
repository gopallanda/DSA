def longestSubstringDistChar(s, k):
    freq = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        # shrink window when distinct > k
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

if __name__=="__main__":
    s=input("Enter the string: ")
    k=int(input("Enter the value of k: "))
    res=longestSubstringDistChar(s,k)
    print(res)