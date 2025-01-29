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
    # TODO: Implement this function
    if not head:
        return 
    curr = head 
    before = None 
    after = curr
    while after:
        after = curr.next 
        curr.next = before
        before = curr
        curr = after
    return before
    