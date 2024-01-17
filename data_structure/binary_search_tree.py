class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value):
        self.root = Node(value)
    
    def search(self, value):
        cur_node = self.root
        while True:
            if cur_node.value == value:
                return cur_node
            elif cur_node.value > value:
                if cur_node.left != None:
                    cur_node = cur_node.left
                else:
                    return None
            else:
                if cur_node.right != None:
                    cur_node = cur_node.right
                else:
                    return None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
        else:
            cur_node = self.root
            while True:
                if value < cur_node.value:
                    if cur_node.left == None:
                        cur_node.left = new_node
                        break
                    else:
                        cur_node = cur_node.left
                else:
                    if cur_node.right == None:
                        cur_node.right = new_node
                        break
                    else:
                        cur_node = cur_node.right
                        break

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, root, value):
        if root is None:
            return root
        if value < root.value:
            root.left = self._delete_recursive(root.left, value)
        elif value > root.value:
            root.right = self._delete_recursive(root.right, value)
        else:
            if root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            root.value = self._get_min_value(root.right)
            root.right = self._delete_recursive(root.right, root.value)
        return root

    def _get_min_value(self, root):
        while root.left is not None:
            root = root.left
        return root.data

# 중위순회로 테스트케이스 확인 !!!
def print_inorder(root):
    if root != None:
        print_inorder(root.left)
        print(f'{root.value}')
        print_inorder(root.right)

root = Node(1)
bst = BinarySearchTree(root)
bst.insert(2)
bst.insert(7)
bst.insert(8)
bst.insert(10)
print(bst.search(2)) // True
print(bst.search(5)) // False
print(bst.search(7)) // True
print(bst.search(8)) // True
print(bst.search(15)) // False