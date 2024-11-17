def permuteUnique(nums):
    # T = O(n!)
    # S = O(n * n!)
    res = [] 
    def helper(idx):
        if idx == len(nums) - 1:
            res.append(nums[:]) # get copy in res list
            return 
        hash_map = {}
        for j in range(idx, len(nums)):
            if nums[j] not in hash_map:
                hash_map[nums[j]] = True 
                nums[idx], nums[j] = nums[j], nums[idx]
                helper(idx + 1)
                nums[idx], nums[j] = nums[j], nums[idx]
    helper(0)
    return res 
    
print(permuteUnique([1,1,2]))


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([2, 2, 1], [[2, 2, 1], [2, 1, 2], [1, 2, 2]]),
        ([1], [[1]]),
        ([1, 2, 2, 3], [
            [1, 2, 2, 3], [1, 2, 3, 2], [1, 3, 2, 2], [2, 1, 2, 3], [2, 1, 3, 2], 
            [2, 2, 1, 3], [2, 2, 3, 1], [2, 3, 1, 2], [2, 3, 2, 1], [3, 1, 2, 2], 
            [3, 2, 1, 2], [3, 2, 2, 1]
        ])
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = permuteUnique(nums)
        print(f"Test case {i}: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'Passed' if sorted(result) == sorted(expected) else 'Failed'}\n")