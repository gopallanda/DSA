from collections import deque
class Queue:
    def __init__(self):
        self.d1=deque()
        self.d2=deque()
    def enque(self,data):
        self.d1.append(data)
    def deque(self,k):
        if len(self.d1)<k:
            print(f"error: {k} is larger than size of the queue")
            return 
        else:
            while k>0:
                self.d2.append(self.d1.popleft())
                k-=1
            self.d2.reverse()
        
    def reverse(self):
         self.d2.extend(self.d1)
         return self.d2
if __name__=="__main__":
    n=int(input("enter size of the queue:"))
    q=Queue()
    print("enter queue elements: ")
    for i in range(n):
        num=int(input())
        q.enque(num)
    k=int(input("enter k value: "))
    q.deque(k)
    res=q.reverse()
    print(res)
    