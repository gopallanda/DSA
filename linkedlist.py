class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def Traverse(self):
        temp = self.head
        while temp.next:
            print(temp.data, end=" -> ")
            temp = temp.next
        print(temp.data)

    def addBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def addPosition(self, data, pos):
        new_node = Node(data)

        if pos == 0:
            new_node.next = self.head
            self.head = new_node
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
        temp.next = new_node
    def deleteNodeBegin(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
    def deleteNodeEnd(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
    def deleteNodePosition(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 0:
            self.head = self.head.next
            return
        temp = self.head
        for i in range(pos - 1):
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp = temp.next
        if temp.next is None:
            print("Position out of range")
            return
        temp.next = temp.next.next
    def deleteNodeValue(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next
        if temp.next is None:
            print("Value not found in the list")
            return
        temp.next = temp.next.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.addEnd(1)
    ll.addEnd(2)
    ll.addEnd(3)
    ll.Traverse()  # Output: 1 -> 2 -> 3
    ll.addBegin(9)
    ll.addPosition(8, 1)
    ll.Traverse()  # Output: 9 -> 1 -> 8 -> 2 -> 3
    ll.deleteNodeBegin()
    ll.Traverse()  # Output: 1 -> 8 -> 2 ->
    ll.deleteNodeEnd()
    ll.Traverse()  # Output: 1 -> 8 -> 2
    ll.deleteNodePosition(1)  
    ll.Traverse()  # Output: 1 -> 2
    ll.deleteNodeValue(2)
    ll.Traverse()  # Output: 2