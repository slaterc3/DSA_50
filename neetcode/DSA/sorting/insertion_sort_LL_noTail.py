# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Create the dummy node for the new sorted list
        # It's good practice to use a value that's out of bounds, like -infinity
        dummy = ListNode(-5001) # -5001 is less than any problem constraint
        
        current = head # This is the node we're trying to insert
        
        # 2. Outer loop: Iterate through the original list
        while current:
            
            # Store the next node to process from the original list
            # We must do this BEFORE we change current.next
            next_node_to_process = current.next
            
            # 3. Inner loop: Find the correct insertion point in the new list
            # We start from the beginning of the sorted list (dummy) every time
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next
                
            # 4. Insert: Splice 'current' between 'prev' and 'prev.next'
            current.next = prev.next
            prev.next = current
            
            # 5. Move to the next node in the original list
            current = next_node_to_process
            
        # The sorted list starts right after our dummy node
        return dummy.next