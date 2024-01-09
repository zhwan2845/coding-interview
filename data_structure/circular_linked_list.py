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
