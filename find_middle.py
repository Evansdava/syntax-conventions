from math import ceil
from linkedlist import LinkedList


def find_middle(linked_list):
    """Return the middle item of a singly linked list"""
    # Define variables
    curr_node = linked_list.head
    i = 1
    # In case length function is slower than O(1)
    length = linked_list.length()

    # Get to middle node
    while i < ceil(length / 2):
        curr_node = curr_node.next
        i += 1
    # Check whether to return one or two nodes
    if length % 2 != 0:
        return curr_node
    else:
        return (curr_node, curr_node.next)


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4, 5])

    # Expected output: 3
    print(find_middle(ll))

    ll = LinkedList([1, 2, 3, 4, 5, 6])

    # Expected output: (3, 4)
    print(find_middle(ll))
