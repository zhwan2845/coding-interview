class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self, value):
        self.root = Node(value)
    
    def _get_height(self, node: Node) -> int:
        if node == None:
            return 0
        left_height = self._get_height(node.left)
        right_height = self._get_height(node.right)
        return max(left_height, right_height) + 1


    def get_balance_factor(self, node) -> int:
        bf = self._get_height(node.left) - self._get_height(node.right)
        return bf
    
    def rotate_right(self, x: Node) -> Node:
        child = x.left
        cc = child.right
        child.right = x
        x.left = cc
        return child

    def rotate_left(self, x: Node) -> Node:
        child = x.right
        cc = child.left
        child.left = x
        x.right = cc
        return child

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
        self.root = self._insert(self.root, value)

    def _insert(self, node, value) -> Node:
        if node == None:
            node = Node(value)
        if value < node.value:
            node.left =  self._insert(node.left, value)
        elif value > node.value:
            node.right =  self._insert(node.right, value)
        
        if self.get_balance_factor(node) > 1:
            # LL case
            if self.get_balance_factor(node.left) > 0:
                node = self.rotate_right(node)
            # LR case
            else:
                node.left = self.rotate_left(node.left)
                node = self.rotate_right(node)
        elif self.get_balance_factor(node) < -1:
            # RR case
            if self.get_balance_factor(node.right) < 0:
                node = self.rotate_left(node)
            # RL case
            else:
                node.right = self.rotate_right(node.right)
                node = self.rotate_left(node)
        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node: Node, value: int) -> Node: # sub-tree의 root node
        if node == None: # 삭제할 노드가 없는 경우
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
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
        ## LL case
        bf = self.get_balance_factor(node)
        if bf > 1 and self.get_balance_factor(node.left) >= 0:
            node = self.rotate_right(node)
        ## LR case
        elif bf > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            node = self.rotate_right(node)
        ## RR case
        elif bf < -1 and self.get_balance_factor(node.right) <= 0:
            node = self.rotate_left(node)
        ## RL case 
        elif bf < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            node = self.rotate_left(node)
        return node
    
    def inorder(self):
        self._inorder(self.root)
        print()

    def _inorder(self, node: Node):
        if node == None:
            return 
        self._inorder(node.left)
        print(node.value, end='->')
        self._inorder(node.right)
        
if __name__ == '__main__':
    bst = AVLTree(1)
    bst.insert(2)
    bst.inorder()
    bst.insert(7)
    bst.inorder()
    bst.insert(8)
    bst.inorder()
    bst.insert(10)
    bst.inorder()
    bst.delete(2)

    bst.inorder()

    assert bst.search(2) == None
    assert bst.search(5) == None
    
    assert bst.search(7).value == 7
    assert bst.search(8).value == 8
    assert bst.search(15) == None

    