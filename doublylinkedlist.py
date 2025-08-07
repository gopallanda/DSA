class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def addEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def addPosition(self, data, pos):
        new_node = Node(data)
        if pos == 0:
            self.addBegin(data)
            return
        temp = self.head
        for i in range(pos - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def Traverse(self):
        temp = self.head
        while temp.next:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print(temp.data)

    def deleteNodeBegin(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        self.head.prev = None

    def deleteNodeEnd(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def deleteNodePosition(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.deleteNodeBegin()
            return
        temp = self.head
        for i in range(pos):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp is None:
            print("Position out of range")
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def reverseList(self):
        if self.head is None:
            print("List is empty")
            return
        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.addEnd(1)
    ll.addEnd(2)
    ll.addEnd(3)
    ll.Traverse()  # Output: 1 <-> 2 <-> 3 <-> None
    ll.addBegin(0)
    ll.Traverse()  # Output: 0 <-> 1 <-> 2 <-> 3 <-> None
    ll.addPosition(4, 2)
    ll.Traverse()  # Output: 0 <-> 1 <-> 4 <-> 2 <-> 3 <-> None
    ll.deleteNodeBegin()
    ll.Traverse()  # Output: 1 <-> 4 <-> 2 <-> 3 <-> None
    ll.deleteNodeEnd()
    ll.Traverse()  # Output: 1 <-> 4 <-> 2 <-> None
    ll.reverseList()
    ll.Traverse()  # Output: 2 <-> 4 <-> 1 <-> None
