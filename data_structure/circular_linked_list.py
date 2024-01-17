class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_first(self, data):
        if self.head == None:
            new_node = Node(data, None)
            new_node.next = new_node
            self.head = new_node
        else:
            new_node = Node(data, self.head.next)
            self.head.next = new_node
        self.num_of_nodes += 1

    def insert_last(self, data):
        if self.head == None:
            new_node = Node(data, None)
            new_node.next = new_node
            self.head = new_node
        else:
            new_node = Node(data, self.head.next)
            self.head.next = new_node
            self.head = new_node
        self.num_of_nodes += 1
    
    def delete_first(self):
        if self.head == None:
            self.head = None
            return
        elif self.num_of_nodes == 1:
            self.head = None
        else:
            delete_node = self.head.next
            self.head.next = delete_node.next
        self.num_of_nodes -= 1

    def delete_last(self):
        if self.head == None:
            return
        elif self.num_of_nodes == 1:
            self.head = None
        else:
            cur_node = self.head
            while True:
                cur_node = cur_node.next
                if cur_node.next == self.head:
                    break
            cur_node.next = self.head.next
            self.head = cur_node
        self.num_of_nodes -= 1

    def print(self):
        if self.head == None:
            return
        cur_node = self.head
        while True:
            print(f"{cur_node.data} <-> ", end = '')
            cur_node = cur_node.next
            if cur_node == self.head:
                break
        print()

if __name__ == '__main__':
    cl = CircularLinkedList()
    cl.insert_first(3)
    cl.insert_first(2)
    cl.insert_first(1)
    cl.insert_last(4)
    cl.insert_last(5)
    cl.print()
    cl.delete_first()
    cl.delete_last()
    cl.delete_first()
    cl.delete_first()
    cl.print()
    cl.delete_first()
    cl.print()