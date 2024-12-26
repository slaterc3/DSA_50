def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's
    """
    # TODO: Implement this function
    max_1s = 0 
    num_1s = 0
    i = 0
    while i < len(nums):
         
        if nums[i] == 0:
            i += 1 
            num_1s = 0
        else:
            num_1s += 1 
            i += 1 
        max_1s = max(max_1s, num_1s)
    return max_1s
    
print(find_max_consecutive_ones([1,1,0,0,1]))