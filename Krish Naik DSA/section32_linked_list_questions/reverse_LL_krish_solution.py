# Definition for singly linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
def reverse_list(head):
    """
    Function to reverse a singly linked list.
    :param head: ListNode -> head of the singly linked list
    :return: ListNode -> the head of the reversed linked list
    """
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next  # Save next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to this node
        current = next_node       # Move to next node
    
    return prev  # New head of the reversed list
 
# Helper function to display the result (for debugging)
def display_list(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    print(" -> ".join(map(str, values)))
 
# Example usage (can be removed)
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# display_list(reverse_list(head))
