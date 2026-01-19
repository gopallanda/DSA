"""
Question Marks Between Digits
Problem Statement

You are given a string s consisting of lowercase English letters, digits (0–9), and special characters including the question mark (?).

Return true if there exists at least one pair of digits in the string such that there are three or more question mark (?) characters between them.
Otherwise, return false.
Example 1

Input

"wer?r4?jfh5"


Output

false

Example 2

Input

"gh3?ef?e?8ui"


Output

true
"""


def checkQs(strs):
    stack = []
    flag = 0

    for char in strs:
        if char == "?" and flag == 0:
            continue

        if char.isdigit():
            if flag == 0:
                flag = 1
                stack = []  # reset for new digit
            else:
                if len(stack) >= 3:
                    return True  # valid case found
                else:
                    stack = []  # reset for next digit

        if char == "?" and flag == 1:
            stack.append(char)

    return False
if __name__ == "__main__":
    strs = "gh3?ef?e?8ui"
    print(checkQs(strs))  # Output: true