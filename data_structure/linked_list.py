class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    def insert_first(self, data: int):
        # 연결 리스트가 비어있는 경우
        if self.head == None:
            self.head = Node(data, None)
        # 연결 리스트가 비어있지 않은 경우
        else:
            node = Node(data, self.head)
            self.head = node
        self.num_of_nodes += 1

    def insert_last(self, data: int):
        # 연결 리스트가 비어있는 경우
        if self.head == None:
            self.head = Node(data, None)
        # 연결 리스트가 비어있지 않은 경우
        else:
            node = Node(data, None)
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = node
        self.num_of_nodes += 1

    def delete_first(self):
        # 연결 리스트가 비어있는 경우
        if self.head is None:
            return

        self.head = self.head.next
        self.num_of_nodes -= 1

    def delete_last(self):
        # 연결 리스트가 비어있는 경우
        if self.head is None:
            return

        # 마지막 노드를 삭제할 때
        if self.head.next is None:
            self.head = None
        else:
            cur_node = self.head
            while cur_node.next.next is not None:
                cur_node = cur_node.next
            cur_node.next = None
        self.num_of_nodes -= 1

    def print(self):
        if self.head == None:
            return
        cur_node = self.head
        while cur_node != None:
            print(f"{cur_node.data} ->", end=" ")
            cur_node = cur_node.next
        print()

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_first(3)
    ll.insert_first(1)
    ll.insert_last(7)
    ll.insert_last(5)
    ll.print()
    ll.delete_first()
    ll.print()
    ll.delete_last()
    ll.print()
    ll.delete_first()
    ll.print()
    ll.delete_first()
    ll.print()
    ll.delete_last()
    ll.print()

    
    