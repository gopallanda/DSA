def reversePolishNotation(tokens):
    stack=[]
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            a=stack.pop()
            b=stack.pop()
            if token == "+":
                stack.append(b + a)
            elif token == "-":
                stack.append(b - a)
            elif token == "*":
                stack.append(b * a)
            elif token == "/":
                stack.append(int(b / a))
    return stack[0]
if __name__=="__main__":
    tokens=input("enter the tokens:").split()
    result=reversePolishNotation(tokens)
    print("Output:", result)