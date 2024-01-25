import sys
sys.path.append('..')

from data_structure.linked_list import LinkedList

def delete_duplicates(ll: LinkedList):
    """
    Remove duplicates from an unsorted linked list.
    """
    cur = ll.head
    dict = {}
    prev = None
    while cur != None:
        if cur.data in dict:
            prev.next = cur.next
        else:
            dict[cur.data] = True
            prev = cur
        cur = cur.next

if __name__ == '__main__':
    linked_list = LinkedList()
    elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] # 객체

    for element in elements:
        linked_list.insert_last(element)

    delete_duplicates(linked_list)
    linked_list.print()