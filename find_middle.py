from math import ceil

def find_middle(linked_list):
“””Return the middle item of a singly linked list”””
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
