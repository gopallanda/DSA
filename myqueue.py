queue=[1,2,3,4,5]
def push(queue):
    val=eval(input("enter a value: "))
    queue.append(val)
    return queue
def pop(queue):
    if len(queue)<=0:
        print("under flow")
        return queue
    else:
        print(queue.pop(0))
        return queue
push(queue)
print(queue)
pop(queue)
pop(queue)
print(queue)