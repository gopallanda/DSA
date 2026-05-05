class Node():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.length = 0
    def is_empty(self):
        return self.head is None
    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print()
    def add_beg(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length += 1
        self.display()
    def add_end(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            node.prev = temp
        self.length += 1
        self.display()
    def add_pos(self, data, pos):
        if pos < 1 or pos > self.length + 1:
            print("Invalid position")
            return
        if pos == 1:
            self.add_beg(data)
        elif pos == self.length + 1:
            self.add_end(data)
        else:
            node = Node(data)
            temp = self.head
            for _ in range(1, pos - 1):
                temp = temp.next
            node.next = temp.next
            node.prev = temp
            temp.next.prev = node
            temp.next = node
            self.length += 1
            self.display()
    def del_beg(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        self.display()
    def del_end(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.prev.next = None
        self.length -= 1
        self.display()      
    def del_pos(self, pos):
        if pos < 1 or pos > self.length:
            print("Invalid position")
            return
        if pos == 1:
            self.del_beg()
        elif pos == self.length:
            self.del_end()
        else:
            temp = self.head
            for _ in range(1, pos):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.length -= 1
            self.display()
if __name__=="__main__":
    dll = DoublyLinkedList()
    dll.add_end(10)
    dll.add_end(20)
    dll.add_end(30)
    dll.add_beg(5)
    dll.add_pos(15, 3)
    dll.del_beg()
    dll.del_end()
    dll.del_pos(2)