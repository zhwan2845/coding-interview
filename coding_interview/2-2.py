from ..data_structure.linked_list import LinkedList

def nth_to_last(ll: LinkedList, n: int):
    """
    Return nth to last element of a singly linked list.
    """
    if ll.head == None:
        return None
    if n <= 0:
        return None

    slow = fast = ll.head

    # Move fast pointer n nodes ahead
    for _ in range(n):
        if fast is None:
            return None  # n이 리스트의 길이보다 클 경우

        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast.next:
        slow = slow.next
        fast = fast.next

    return slow.data

if __name__ == '__main__':
    # Write your test cases here
    pass