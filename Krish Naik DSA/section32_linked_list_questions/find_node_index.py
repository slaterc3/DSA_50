# Definition for singly linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_index(head, k):
    """
    Function to find the index of a node in a linked list whose value equals k.
    :param head: ListNode -> head of the singly linked list
    :param k: int -> the target value
    :return: int -> index of the node with value k, or -1 if not found
    """
    # TODO: Implement this function
    idx = 0
    if head is None:
        return -1 
    curr = head 
    while curr:
        if curr.val == k:
            return idx 
        curr = curr.next
        idx += 1 
    return -1 
        
        
        
        
        
    
    