import sys
sys.path.append('..')
from data_structure.linked_list import LinkedList

def nth_to_last(ll: LinkedList, n: int):
    """
    Return nth to last element of a singly linked list.
    """
    if ll.head == None:
        return None
    if n <= 0:
        return None

    cur_node = ll.head
    count = 0

    while cur_node:
        count += 1
        cur_node = cur_node.next

    cur_node = ll.head

    for i in range(count - n):
        cur_node = cur_node.next

    return cur_node.data

if __name__ == '__main__':
    # Write your test cases here
    linked_list = LinkedList()
    elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] # 객체

    for element in elements:
        linked_list.insert_last(element)

    print("\nLinked list:", end=" ")
    linked_list.print()
    result = nth_to_last(linked_list, 3)
    print(f"3rd to last element: {result}")