class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
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
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print()

    def add_beg(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
            self.head = node
        self.length += 1
        self.display()

    def add_end(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = node
            node.next = self.head
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
            for i in range(1, pos - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
            self.length += 1
            self.display()

    def del_beg(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        self.length -= 1
        self.display()

    def del_end(self):
        if self.is_empty():
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
            temp.next = self.head
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
            for i in range(1, pos - 1):
                temp = temp.next
            temp.next = temp.next.next
        self.length -= 1
        self.display()


if __name__ == "__main__":
    csll = CircularSinglyLinkedList()
    csll.add_end(10)
    csll.add_end(20)
    csll.add_end(30)
    csll.add_beg(5)
    csll.add_pos(15, 3)
    csll.del_beg()
    csll.del_end()
    csll.del_pos(2)
