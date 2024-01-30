import sys
sys.path.append('..')
from data_structure.linked_list import LinkedList

def sum_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    """
    Sum two linked lists. Each node contains a single digit and the digits are 
    stored in reverse order.

    ll1 = 2 -> 6 -> 1
    ll2 = 5 -> 3 -> 2
    162, 235
    => 397
    => 7 -> 9 > 3
    """
    n1 = 0 # 162
    n2 = 0
    m = 1

    cur_node = ll1.head
    while cur_node != None:
        n1 = n1 + cur_node.data * m
        m = m * 10
        cur_node = cur_node.next

    cur_node = ll2.head
    m = 1
    while cur_node != None:
        n2 = n2 + cur_node.data * m
        m = m * 10
        cur_node = cur_node.next

    sum = n1 + n2 # 397

    result_list = LinkedList() # 7 -> 9 -> 3
    m = 10
    while sum > 0:
        result_list.insert_last(sum % m)
        sum = sum // m
        
    return result_list

if __name__ == '__main__':
    # Write your test cases here
    pass