"""Subsets
Question:

Power Set - Given an integer array of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order."""

def power_set(nums):
    output = [] 
    def helper(nums, idx, subset):
        if idx == len(nums):
            output.append(subset.copy())
            return 
        helper(nums, idx+1, subset)
        subset.append(nums[idx])
        helper(nums, idx+1, subset)
        subset.pop()
    helper(nums, 0, [])
    return output