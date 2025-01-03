def find_first_index(arr, element):
    """
    Function to find the first index of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    int: The first index of the element in the array, or -1 if not found.
    """
    # Your code here
    if len(arr)==0:
        return -1
    if arr[0] == element:
        return 0
    ans = find_first_index(arr[1:], element)
    
    if ans == -1:
        return ans
    else:
        return 1 + ans 
    
print(find_first_index([1,2,3,4,5], 7))
