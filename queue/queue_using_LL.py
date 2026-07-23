class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.front=self.rear=None
    def is_empty(self):
        return self.front is None 
    def display(self):
        if self.is_empty():
            print("list is empty")
        else:
            curr=self.front
            while curr.next:
                print(curr.data,end='->')
                curr=curr.next
            print(curr.data)
            print()
    def enque(self,data):
        node=Node(data)
        if self.is_empty():
            self.front=self.rear=node 
        else:
            self.rear.next=node
            self.rear=node
    def deque(self):
        curr=self.front
        if self.is_empty():
            print("queue is empty")
            return 
        elif self.front==self.rear:
            self.front=self.rear=None
            
        else:
            self.front=self.front.next
        return curr.data
    
    
if __name__=="__main__":
    q=queue()
    q.is_empty()
    q.enque(10)
    q.enque(20)
    q.enque(30)
    q.enque(40)
    q.display()
    x=q.deque()
    q.display()