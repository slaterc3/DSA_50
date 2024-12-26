def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    # TODO: Implement this function
    # intersection = [] 
    s1 = set(nums1)
    s2 = set()
    
    for num in nums2:
        if num in s1:
            s2.add(num)
    l2 = list(s2)
    
    return l2 
    
print(intersection([1,2,3], [4,5,6]))