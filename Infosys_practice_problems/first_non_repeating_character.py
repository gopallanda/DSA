from collections import Counter


def firstNonRepeatingCharacter(s):
    count = Counter(s)

    for ch in s:
        if count[ch] == 1:
            return ch
    return -1
