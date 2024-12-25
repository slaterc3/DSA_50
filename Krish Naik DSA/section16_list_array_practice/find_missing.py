def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    # TODO: Implement this function
    # n = len(nums)
    # h = {i:True for i in range(n+1) if i in nums}
    # l = [i for i in range(n+1) if i not in h]
        
    
    # return h 
    # return l[0]
    
    n = len(nums)
    # Calculate the expected sum of numbers from 0 to n
    expected_sum = n * (n + 1) // 2
    # Calculate the actual sum of the given numbers
    actual_sum = sum(nums)
    
    # The missing number is the difference between the expected sum and the actual sum
    return expected_sum - actual_sum
 
# Helper function to display the result (for debugging)


print(find_missing_number([3,0,1]))