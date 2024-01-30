class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)
    
    def search(self, value): 
        return self._search(self.root, value)
    
    def _search(self, node, value) -> Node:
        if node == None:
            return None
        if value < node.value:
            return self._search(node.left, value)
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return node

    def insert(self, value):
        return self._insert(self.root, value)

    def _insert(self, node, value) -> Node:
        if node == None:
            node = Node(value)
        if value < node.value:
            node.left =  self._insert(node.left, value)
        elif value > node.value:
            node.right =  self._insert(node.right, value)
        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    # 재귀 함수로 구현하기
    def _delete(self, node: Node, value: int) -> Node: # sub-tree의 root node
        if node == None: # 삭제할 노드가 없는 경우
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
            return node
        elif value > node.value:
            node.right = self._delete(node.right, value)
            return node
        else: # 찾은 경우
            # 자식이 0개 있는 경우
            if node.left == None and node.right == None:
                return None
            # 자식이 1개 있는 경우
            elif node.left == None and node.right != None:
                return node.right
            elif node.left != None and node.right == None:
                return node.left
            # 자식이 2개 있는 경우
            else:
                cur_node = node.right
                parent_node = None
                while cur_node.left != None:
                    parent_node = cur_node
                    cur_node = cur_node.left
                node.value = cur_node.value
                parent_node.left = cur_node.right
                return node
                
if __name__ == '__main__':
    bst = BinarySearchTree(1)
    bst.insert(2)
    bst.insert(7)
    bst.insert(8)
    bst.insert(10)
    bst.delete(2)
    print()

    print(bst.search(2)) # False
    print(bst.search(5)) # False
    print(bst.search(7).value) # True
    print(bst.search(8).value) # True
    print(bst.search(15)) # False