def longestRepeatingCharacter(s, k):
    left = 0
    max_freq = 0
    count = {}
    result = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_fre = max(max_freq, count[s[r]])
        while (r - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        result = max(result, r - left + 1)
    return result


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    print(longestRepeatingCharacter(s, k))  # Output: 4
