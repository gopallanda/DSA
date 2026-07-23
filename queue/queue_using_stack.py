from collections import deque
class queueUsingStack:
    def __init__(self) -> None:
         self.s1=deque()
         self.s2=deque()
        
    def enque(self,data):
        self.s1.append(data)
    def deque(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        if not self.s2:
            print("queue is empty")
            return 
        return self.s2.pop()
    
                