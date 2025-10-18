# solution.py

# Import the class definition from the separate file
from listnode import ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Your iterative reversal logic (or any other list operation)
        prev = None 
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        return prev

# Example usage (for testing)
if __name__ == "__main__":
    # Create a list 1 -> 2 -> 3
    original_list = ListNode.from_list([1, 2, 3, 4, 5])
    
    # Reverse it
    reversed_list = Solution().reverseList(original_list)
    
    # Print the result (if you included the __repr__ method)
    # This part would typically be handled in a separate test script
    print(reversed_list)