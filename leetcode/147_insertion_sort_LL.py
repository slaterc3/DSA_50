# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # Dummy node simplifies edge cases
        dummy = ListNode(0)
        dummy.next = head
        curr = head.next
        head.next = None  # first node is already "sorted"
        
        while curr:
            # Save the next node before changing links
            next_temp = curr.next

            # Find the position to insert `curr`
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            
            # Insert `curr` between prev and prev.next
            curr.next = prev.next
            prev.next = curr

            # Move on
            curr = next_temp
        
        return dummy.next
