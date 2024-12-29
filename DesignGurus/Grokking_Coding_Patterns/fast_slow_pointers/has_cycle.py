#class Node:
#  def __init__(self, value, next=None):
#    self.val = value
#    self.next = next

class Solution:
  def hasCycle(self, head):
    # TODO: Write your code here
    fast = head 
    slow = head 
    while fast != None and fast.next != None:
      slow = slow.next 
      fast = fast.next.next 
      if slow == fast:
        return True 
    return False
