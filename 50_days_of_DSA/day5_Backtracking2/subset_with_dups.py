"""Coding Exercise: Subsets 2
Given an integer array nums that may contain duplicates, return all possible

subsets

(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example : 

nums = [1,3,3]

Output = [ [], [1], [3], [1,3], [3,3], [1,3,3] ]"""

def subset_with_duplicates(nums):
    # nums.sort()
    res = [] 
    
    def helper(idx, curr):
        if idx == len(nums):
            res.append(curr[:])
            return
        # include block 
        curr.append(nums[idx])
        helper(idx+1, curr)
        curr.pop()
        # exclude block 
        if idx < len(nums)-1 and nums[idx] == nums[idx+1]:
            idx += 1 
        helper(idx+1, curr)
    helper(0, [])
    return res 

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]),
        ([1, 2, 3], [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]),
        ([2, 2, 2], [[], [2], [2, 2], [2, 2, 2]]),
        ([], [[]]),
        ([1], [[], [1]]),
        ([1, 1, 1, 1], [[], [1], [1, 1], [1, 1, 1], [1, 1, 1, 1]])
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        result = subset_with_duplicates(nums)
        print(f"Test case {i}: nums = {nums}")
        print(f"Expected: {sorted(expected)}")
        print(f"Got: {sorted(result)}")
        print(f"{'Passed' if sorted(result) == sorted(expected) else 'Failed'}\n")