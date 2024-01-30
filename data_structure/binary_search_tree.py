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

    def delete(self, value):
        pass

if __name__ == '__main__':
    bst = BinarySearchTree(1)
    bst.insert(2)
    bst.insert(7)
    bst.insert(8)
    bst.insert(10)
    bst.delete(2)
    print_inorder(bst.root)
    print()

    print(bst.search(2)) # False
    print(bst.search(5)) # False
    print(bst.search(7)) # True
    print(bst.search(8)) # True
    print(bst.search(15)) # False