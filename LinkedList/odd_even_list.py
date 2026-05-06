class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def oddEvenList(head):
    if not head or not head.next:
        return head 
    odd=head
    even=head.next
    evenHead=even 
    while even and even.next:
        odd.next=even.next
        odd=odd.next 
        even.next=odd.next
        even=even.next 
    odd.next=evenHead
    return head

if __name__=="__main__":
    ll=LinkedList()
    n=int(input("Enter the number of nodes: "))
    for _ in range(n):
        data=int(input("Enter the node data: "))
        ll.append(data)
    print("Original list:")
    ll.display()
    ll.head=oddEvenList(ll.head)
    print("Modified list:")
    ll.display()