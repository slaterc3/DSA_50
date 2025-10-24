# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # 1. Dummy head for the new sorted list
        dummy = ListNode(-5001) 
        
        # 2. Tail pointer for the new sorted list
        sorted_tail = dummy
        
        current = head # Node to insert from the original list
        
        while current:
            # Store the next node before we change pointers
            next_node_to_process = current.next 
            
            # --- OPTIMIZATION CHECK ---
            # If current node's value is >= tail's value,
            # it's the new tail. This is an O(1) operation.
            if current.val >= sorted_tail.val:
                sorted_tail.next = current
                sorted_tail = current
                # Detach the node from any following nodes
                current.next = None 
            
            # --- NORMAL INSERTION ---
            # Otherwise, we must find its spot from the beginning
            else:
                prev = dummy
                # Find the node right BEFORE the insertion point
                while prev.next and prev.next.val < current.val:
                    prev = prev.next
                    
                # Splice 'current' between 'prev' and 'prev.next'
                current.next = prev.next
                prev.next = current
            
            # Move to the next node in the original list
            current = next_node_to_process
            
        return dummy.next