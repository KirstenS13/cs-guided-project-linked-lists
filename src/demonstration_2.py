"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""

# So basically we want the pointers pointing this way <-- not this way -->
#   we're reversing the direction of the pointer, not the order of the list

class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head_of_list):
    # soln that was in here before lecture
    # current_node = head_of_list
    # previous_node = None
    # next_node = None

    # # Until we have 'fallen off' the end of the list
    # while current_node:
    #     # Copy a pointer to the next element
    #     # before we overwrite current_node.next
    #     next_node = current_node.next

    #     # Reverse the 'next' pointer
    #     current_node.next = previous_node

    #     # Step forward in the list
    #     previous_node = current_node
    #     current_node = next_node

    # return previous_node

    # soln from lecture
    # reverse all the pointers:
    # loop (while) go while... we still have nodes to process
    # we have a current_node
    # initialize current_node
    current_node = head_of_list
    # we need a reference to prev
    # when we start, prev is none
    prev = None

    # on each iteration of the loop:
    while current_node is not None:
        print("current node:", current_node.value)
    # we need a reference to next_node:
    # next_node = current_node.next
        next_node = current_node.next
    # set current_node.next to prev
        current_node.next = prev
    # set prev to cur_node
        prev = current_node
    # update current_node to point to next_node
        current_node = next_node

    return current_node

x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

cur_node = x
while cur_node:
    print(cur_node.value)
    cur_node = cur_node.next
    
print("------")
new_head = reverse(x)
print(new_head)
#
# print("reversed list:")
# cur_node = new_head
# while cur_node:
#     print(cur_node.value)
#     cur_node = cur_node.next

# print("-----")
# print(x.value, x.next)
# print(y.value, y.next.value)
# print(z.value, z.next)