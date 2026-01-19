'''
Problem Statement: Third Largest String by Length
Problem Description

You are given an array of strings strArr consisting of lowercase English letters.
Your task is to find and return the third largest string based on length.

Ordering Rules

Strings must be ranked in descending order of length.

If two or more strings have the same length, the string that appears later in the original array should be ranked higher.

Input:
strArr = ['abc', 'gefd', 'x', 'abcds', 'def']

Output:
'def'

'''

def thirdLargest_string(strArr):
    strArr.sort(key=lambda x: (len(x)))
    third_max_len=len(strArr[-3])
    candidates=[s for s in strArr if len(s)==third_max_len]
    return candidates[-1]

if __name__ == "__main__":
    strArr = ['abc', 'gefd', 'x', 'abcds', 'def']
    print(thirdLargest_string(strArr))  # Output: 'def'