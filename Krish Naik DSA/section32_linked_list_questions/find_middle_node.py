# Definition for singly linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_middle(head):
    """
    Function to find the middle node of a singly linked list.
    :param head: ListNode -> head of the singly linked list
    :return: ListNode -> the middle node of the linked list
    """
    # TODO: Implement this function
    if head is None:
        return 
    fast = head 
    slow = head 
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next 
    return slow 
    
    