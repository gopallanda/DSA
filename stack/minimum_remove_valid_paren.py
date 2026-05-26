
def minimumRemoveToMakeValid(s: str) -> str:
    S=list(s)
    stack = []
    for i, char in enumerate(S):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                S[i] = ''

    while stack:
        S[stack.pop()] = ''

    return ''.join(S)
if __name__=="__main__":
    s='le(e)t(c)o)de)'
    result=minimumRemoveToMakeValid(s)
    print("the string after removing the minimum number of parentheses to make it valid:",result)