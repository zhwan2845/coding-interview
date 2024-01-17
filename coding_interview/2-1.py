from data_structure.linked_list import LinkedList

def delete_duplicates(ll: LinkedList):
    """
    Remove duplicates from an unsorted linked list.
    """
    if ll.head is None:
        return

    cur_node = ll.head
    seen_values = {cur_node.data}

    while cur_node.next:
        if cur_node.next.data == seen_values:
            cur_node.next = cur_node.next.next
        else:
            seen_values.add(cur_node.next.data)
            cur_node = cur_node.next

if __name__ == '__main__':
    linked_list = LinkedList()
    elements = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    for element in elements:
        linked_list.append(element)

    delete_duplicates(linked_list)
    linked_list.display()