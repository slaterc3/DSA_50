# Definition for singly linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_elements(head, val):
    """
    Function to remove all nodes with value val from the linked list.
    :param head: ListNode -> head of the singly linked list
    :param val: int -> the value to be removed
    :return: ListNode -> the head of the new linked list
    """
    # TODO: Implement this function
    if head is None:
        return 
    while head and head.val == val:
        head = head.next 
    curr = head 
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next 
        else:
            curr = curr.next 
    return head 
    
def create_linked_list(lst):
    """Helper function to create a linked list from a Python list."""
    if not lst:
        return None
    head = ListNode(lst[0])
    curr = head
    for val in lst[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head):
    """Helper function to convert a linked list to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

    
        
# Test case 1: Remove elements from a mixed list
head = create_linked_list([1, 2, 6, 3, 4, 5, 6])
new_head = remove_elements(head, 6)
print(linked_list_to_list(new_head))  # Expected: [1, 2, 3, 4, 5]

# Test case 2: Remove all elements (list becomes empty)
head = create_linked_list([6, 6, 6, 6])
new_head = remove_elements(head, 6)
print(linked_list_to_list(new_head))  # Expected: []

# Test case 3: No elements to remove
head = create_linked_list([1, 2, 3, 4, 5])
new_head = remove_elements(head, 6)
print(linked_list_to_list(new_head))  # Expected: [1, 2, 3, 4, 5]

# Test case 4: Empty list
head = create_linked_list([])
new_head = remove_elements(head, 1)
print(linked_list_to_list(new_head))  # Expected: []

# Test case 5: Only one node, and it matches the target value
head = create_linked_list([1])
new_head = remove_elements(head, 1)
print(linked_list_to_list(new_head))  # Expected: []

# Test case 6: Only one node, and it does not match the target value
head = create_linked_list([1])
new_head = remove_elements(head, 2)
print(linked_list_to_list(new_head))  # Expected: [1]
