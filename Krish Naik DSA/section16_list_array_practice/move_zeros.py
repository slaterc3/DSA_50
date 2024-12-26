def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    # TODO: Implement this function
    non_zero_idx = 0 
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_idx] = nums[i]
            non_zero_idx += 1 
    
    while non_zero_idx < len(nums):
        nums[non_zero_idx] = 0 
        non_zero_idx += 1 
    
    print(nums)
        
        
        
print(move_zeroes([0,1,0,3,12]))