from listnode import ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base Case: If the list is empty (None) or has only one node, 
        # it is already reversed.
        if head is None or head.next is None:
            return head
        
        # 1. Recursively reverse the rest of the list starting from head.next.
        #    'new_head' will be the tail of the original list, 
        #    which becomes the new head of the fully reversed list.
        new_head = self.reverseList(head.next)
        
        # 2. Reverse the link: Make the second node (head.next) point back to the first node (head).
        head.next.next = head
        
        # 3. Disconnect the old link: Make the current head (which is now the tail) point to None.
        head.next = None
        
        # 4. Return the new head (the original tail).
        return new_head