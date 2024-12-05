def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # lst = []
    # for i in range(len(nums)-1):
    #     for j in range(i+1,len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return []
    h = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in h:
            return [h[diff], i]
        h[n] = i 
    return 
    
print(twoSum([2,3,11,5], 13))