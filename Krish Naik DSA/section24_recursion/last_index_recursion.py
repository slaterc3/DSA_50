def lastIndexOfAnElement(l1, x):
    # Base case: if the list is empty, return -1
    if len(l1) == 0:
        return -1

    # Recursive call on the rest of the list (excluding the first element)
    ansFromRecursion = lastIndexOfAnElement(l1[1:], x)

    # If the element is found in the rest of the list, return the adjusted index
    if ansFromRecursion != -1:
        return ansFromRecursion + 1

    # If the element is not found in the rest of the list, check the current element
    if l1[0] == x:
        return 0

    # If not found anywhere, return -1
    return -1

print(lastIndexOfAnElement([1,2,3,4,5,2,1], 2)) # should print 5

# lastIndexOfAnElement([3, 2, 5, 2, 8, 2, 1], 2)
#   |
#   --> lastIndexOfAnElement([2, 5, 2, 8, 2, 1], 2)
#         |
#         --> lastIndexOfAnElement([5, 2, 8, 2, 1], 2)
#               |
#               --> lastIndexOfAnElement([2, 8, 2, 1], 2)
#                     |
#                     --> lastIndexOfAnElement([8, 2, 1], 2)
#                           |
#                           --> lastIndexOfAnElement([2, 1], 2)
#                                 |
#                                 --> lastIndexOfAnElement([1], 2)
#                                       |
#                                       --> lastIndexOfAnElement([], 2)
#                                             --> Base Case: Return -1
#                                 |
#                                 --> l1[0] == 2 --> Return 0
#                           |
#                           --> Adjust Index: 0 + 1 --> Return 1
#                     |
#                     --> Adjust Index: 1 + 1 --> Return 2
#               |
#               --> Adjust Index: 2 + 1 --> Return 3
#         |
#         --> Adjust Index: 3 + 1 --> Return 4
#   |
#   --> Adjust Index: 4 + 1 --> Return 5
