stack=[1,2,3,4,5,6]
def push(stack):
    val=eval(input("enter a value: "))
    stack.append(val)
    return stack    
    
def pop(stack):
    if len(stack)<=0:
        print("underflow")
        return stack   
    else:
        print(stack.pop())
        return stack
push(stack)
print(stack)
pop(stack)
print(stack)
pop(stack)