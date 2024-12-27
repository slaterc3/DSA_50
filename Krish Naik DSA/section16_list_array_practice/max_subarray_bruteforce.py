def max_subarray_sum_brute_force(arr):
    """
    Brute-force approach to find the maximum sum of any subarray.

    Parameters:
    arr (List[int]): List of integers.

    Returns:
    int: Maximum sum of any subarray.
    """
    if len(arr) == 0:
        return 0  # Handle empty array case
    
    max_sum = float('-inf')  # Initialize to negative infinity to handle all-negative arrays

    # Iterate over all possible starting points
    for i in range(len(arr)):
        current_sum = 0  # Reset current sum for each starting point
        # Iterate over all possible ending points
        for j in range(i, len(arr)):
            # Calculate the sum of the subarray from i to j
            current_sum += arr[j]
            # Update the maximum sum
            max_sum = max(max_sum, current_sum)
    
    return max_sum