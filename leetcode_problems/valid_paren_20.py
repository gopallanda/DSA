def validParens(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != stack[-1]:
                return False
            stack.pop()
        else:
            return False
    return not stack


if __name__ == "__main__":
    s = "()[]{}"
    print(validParens(s))  # Output: True
