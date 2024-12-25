def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    
    n = len(lst)
    for i in range(n//2):
        temp = lst[i]
        lst[i] = lst[-(i+1)]
        lst[-(i+1)] = temp
    
    return lst 

# def reverse_list(lst):
#     """
#     Function to reverse the order of elements in a list.
#     :param lst: List[int] -> List of integers
#     :return: List[int] -> The list with elements in reversed order
#     """
#     left = 0
#     right = len(lst) - 1
    
#     # Swap elements from start and end moving towards the center
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
    
#     return lst
print(reverse_list([1,2,3,4,5]))
print(reverse_list([1,2,3,4]))