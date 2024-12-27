def max_subarray_sum(arr):
    """
    Given an array of integers, find the maximum sum of any subarray.

    Parameters:
    arr (List[int]): List of integers.

    Returns:
    int: Maximum sum of any subarray.
    """
    # Implement the function
    if len(arr) == 0:
        return 0 
    
    max_ending_here = 0 
    max_so_far = float('-inf')
    
    for num in arr:
        max_ending_here = max(num, max_ending_here+num)
        max_so_far = max(max_ending_here, max_so_far)
    return max_so_far
    
