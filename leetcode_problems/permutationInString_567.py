from collections import Counter


def checkInclusion(s1, s2):
    k = len(s1)
    s1_count = Counter(s1)
    window = Counter(s2[:k])
    if s1_count == window:
        return True
    for i in range(k, len(s2)):
        window[s2[i]] += 1
        window[s2[i - k]] -= 1
        if window[s2[i - k]] == 0:
            del window[s2[i - k]]
        if s1_count == window:
            return True
    return False
