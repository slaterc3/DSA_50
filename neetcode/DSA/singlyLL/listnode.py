# listnode.py

from typing import Optional

class ListNode:
    """
    Definition for singly-linked list node.
    """
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    # Optional: Add a helper method for better printing/debugging
    def __repr__(self):
        return f"ListNode(val={self.val}, next={self.next.val if self.next else 'None'})"

    # Optional: Add a helper method to easily convert list to linked list
    @staticmethod
    def from_list(data: list) -> Optional['ListNode']:
        if not data:
            return None
        
        head = ListNode(data[0])
        current = head
        for val in data[1:]:
            current.next = ListNode(val)
            current = current.next
        return head