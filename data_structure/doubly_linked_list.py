class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_first(self, value):
        new_node = Node(value, None, None)
        # 연결 리스트가 비어 있는 경우
        if self.head == None: 
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node
        self.num_of_nodes += 1

    def insert_last(self, value):
        new_node = Node(value, None, None)
        if self.head == None:
            new_node.prev = new_node
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
        self.num_of_nodes += 1

    def delete_first(self):
        # 연결 리스트가 비어있는 경우
        if self.head == None:
            print("List is empty. Nothing to delete.")
            return
        # 연결 리스트에 노드가 한 개 있는 경우
        if self.head.next == self.head:
             self.head = None
        else:
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next
        self.num_of_nodes -= 1

    def delete_last(self):
        if self.head == None:
            print("List is empty. Nothing to delete.")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            self.head.prev = self.head.prev.prev
            self.head.prev.next = self.head
        self.num_of_nodes -= 1

    def display(self):
        if self.head == None:
            return
        cur_node = self.head
        while True:
            print(f"{cur_node.data} <-> ", end='')
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        print()

if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.insert_first(3)
    dll.insert_first(2)
    dll.insert_first(1)
    dll.insert_last(4)
    dll.insert_last(5)
    dll.display()  # Output: 1 <-> 2 <-> 3 <-> 4 <-> 5
    dll.delete_first()
    dll.delete_last()
    dll.display()