"""Coding Exercise ( Permutations)
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

nums = [1,4]

Output :[[1,4],[4,1]]

Example 2:

nums = [1,4,5]

Output :[[1,4,5],[1,5,4],[4,1,5],[4,5,1],[5,1,4],[5,4,1]]"""

def permute(nums):
    if not nums:
        return [[]]
    n = len(nums)
    # using helper function
    res = []
    def helper(idx):
        if idx == n-1:
            # appending copy of `nums`
            res.append(nums[:])
            return # simply return here
        for j in range(idx, n):
            # swapping the first time
            nums[idx], nums[j] = nums[j], nums[idx]
            # call the helper with idx incremented 1
            helper(idx+1)
            # the backtracking step to get to square one
            nums[idx], nums[j] = nums[j], nums[idx]
    helper(0)
    return res 
    
if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]),
        ([1, 2], [[1, 2], [2, 1]]),
        ([1], [[1]]),
        ([], [[]]),  # Edge case: empty list has only one permutation, which is the empty list itself
        ([0, 1], [[0, 1], [1, 0]]),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = permute(nums)
        print(f"Test case {i}: nums = {nums}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print("Passed" if result == expected else "Failed", "\n")