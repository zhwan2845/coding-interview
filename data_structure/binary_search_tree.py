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
                return True
            elif cur_node.value > value:
                if cur_node.left != None:
                    cur_node = cur_node.left
                else:
                    return False
            else:
                if cur_node.right != None:
                    cur_node = cur_node.right
                else:
                    return False

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

    def delete(self, value):
        pass

# 중위순회로 테스트케이스 확인 !!!
def print_inorder(root):
    if root != None:
        print_inorder(root.left)
        print(f'{root.value}',end=' ')
        print_inorder(root.right)
        # 반복문
        top = -1
        def push(root):
            if 
        def pop():
            
        while True:
            for root in range(None):
                push(root)
                root = root.left
            root = pop()

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