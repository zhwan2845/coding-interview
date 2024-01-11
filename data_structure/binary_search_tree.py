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
        if not self.root:
            self.root = new_node
        else:
            cur_node = self.root
            while True:
                if value < cur_node.value:
                    if cur_node.left is None:
                        cur_node.left = new_node
                        break
                    else:
                        cur_node = cur_node.left
                elif value > cur_node.value:
                    if cur_node.right is None:
                        cur_node.right = new_node
                        break
                    else:
                        cur_node = cur_node.right
                else:
                    break

    def delete(self, value):
        def find_min(node):
            while node.left:
                node = node.left
            return node

        def _delete(root, key):
            if not root:
                return None

            if key < root.value:
                root.left = _delete(root.left, key)
            elif key > root.value:
                root.right = _delete(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left

                # 두 자식을 가진 경우, 오른쪽 서브트리에서 최소 값을 찾아서 현재 노드와 교체
                successor = find_min(root.right)
                root.value = successor.value
                root.right = _delete(root.right, successor.value)

            return root

        self.root = _delete(self.root, value)
