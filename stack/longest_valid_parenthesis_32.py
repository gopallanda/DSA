''' longest valid parentheses leetcode 32, in this problem we are given a string of parentheses and we need to find the longest valid parentheses substring. We can solve this problem using a stack. We will iterate through the string and for each character we will check if it is an opening parenthesis or a closing parenthesis. If it is an opening parenthesis we will push its index onto the stack. If it is a closing parenthesis we will pop the top element from the stack and check if it is an opening parenthesis. If it is an opening parenthesis we will calculate the length of the valid parentheses substring and update the maximum length if necessary. If it is not an opening parenthesis we will push the index of the closing parenthesis onto the stack. Finally, we will return the maximum length of the valid parentheses substring. example input: "(()())" output: 6
'''

def longestValidParentheses(s):
    stack=[]
    last_invalid=-1
    max_len=0
    for i, ch in enumerate(s):
        if ch=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
                if stack:
                    max_len=max(max_len, i-stack[-1])
                else:
                    max_len=max(max_len, i-last_invalid)
            else:
                last_invalid=i
    return max_len
# The above function returns the length of the longest valid parentheses substring. If we also want to return the longest valid parentheses substring itself, we can modify the function as follows:


def longestValidParenthesesString(s):
    stack=[]
    last_invalid=-1
    max_len=0
    res=''
    for i, ch in enumerate(s):
        if ch=='(':
            stack.append(i)
        else:
            if stack:
                res+=s[stack.pop()]
                res+=ch
                if stack:
                    max_len=max(max_len, i-stack[-1])
                else:
                    max_len=max(max_len, i-last_invalid)
            else:
                last_invalid=i
    return max_len,res

if __name__=="__main__":
    s=input("enter string of parentheses: ")
    res=longestValidParentheses(s)
    print(res)
    length,string=longestValidParenthesesString(s)
    print(length,string)