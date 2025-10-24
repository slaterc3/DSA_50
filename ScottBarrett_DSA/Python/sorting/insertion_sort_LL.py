class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE INSERTION_SORT METHOD HERE #
    
    def insertion_sort(self):
        if self.length <= 1:
            return 
        dummy = Node(-1)
        curr = self.head
        sorted_tail = dummy 
        while curr:
            nxt = curr.next 
            # sorted_tail = dummy 
            if curr.value >= sorted_tail.value:
                sorted_tail.next = curr
                sorted_tail = curr 
                curr.next = None 
            else:
                prev = dummy 
                while prev.next and prev.next.value < curr.value:
                    prev = prev.next 
                curr.next = prev.next 
                prev.next = curr 
            curr = nxt 
        self.tail = sorted_tail 
        self.head = dummy.next 
        return self.head
    
    
    ####################################





my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

