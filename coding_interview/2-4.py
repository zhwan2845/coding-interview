import sys
sys.path.append('..')
from data_structure.linked_list import LinkedList

def partition(ll: LinkedList, x: int):
    """
    Partition a linked list around a value x, such that all nodes less than x 
    come before all nodes greater than or equal to x.
    """
    less_than_x = LinkedList()  # x보다 작은 노드들을 저장할 연결 리스트
    greater_than_equal_x = LinkedList()  # x보다 크거나 같은 노드들을 저장할 연결 리스트

    # 기존 연결 리스트를 순회하면서 노드를 두 그룹으로 분리
    cur_node = ll.head
    while cur_node != None:
        if cur_node.data < x:
            less_than_x.insert_last(cur_node.data)
        else:
            greater_than_equal_x.insert_last(cur_node.data)
        cur_node = cur_node.next

    # 두 그룹의 연결 리스트를 연결하여 새로운 연결 리스트 생성
    result_linked_list = LinkedList()
    if less_than_x.head != None:
        result_linked_list.head = less_than_x.head
        less_than_x_last_node = less_than_x.head
        while less_than_x_last_node.next != None:
            less_than_x_last_node = less_than_x_last_node.next
        less_than_x_last_node.next = greater_than_equal_x.head
    else:
        result_linked_list.head = greater_than_equal_x.head

    # 결과 연결 리스트의 노드 개수 업데이트
    result_linked_list.num_of_nodes = ll.num_of_nodes

    return result_linked_list


if __name__ == '__main__':
    # Write your test cases here
    linked_list = LinkedList()
    linked_list.insert_last(3)
    linked_list.insert_last(5)
    linked_list.insert_last(8)
    linked_list.insert_last(5)
    linked_list.insert_last(10)
    linked_list.insert_last(2)
    linked_list.insert_last(1)
    linked_list.print()
    
    partitioned_list = partition(linked_list, 5)
    partitioned_list.print()
