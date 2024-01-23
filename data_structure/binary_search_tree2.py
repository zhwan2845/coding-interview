class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)
    
    def search(self, value):
        pass

    def insert(self, value):
        pass

    # root를 반환하기
    def delete(self, value) -> Node:
        return self._delete(self.root, value)
        
    def _delete(self, node: Node, value: int) -> Node:
        if value < node.value:
            node.left = self._delete(self, node.left, value)
        elif value > node.value:
            node.right = self._delete(self, node.right, value)
        else:
            # 삭제하는 부분
            # 1. 자식이 0개있는경우
            if node.left == None and node.right == None:
                del node # free(node)
                return None
            # 2. 자식이 1개있는 경우
            if node.left == None and node.right != None:
                return node.right
            elif node.left != None and node.right == None:
                return node.left
            # 3. 자식이 2개있는 경우
            else:
                cur_node = node.right
                while cur_node.left != None:
                    cur_node = cur_node.left
                
            

if __name__ == '__main__':
    pass