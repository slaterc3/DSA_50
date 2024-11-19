"""Coding Exercise: Subsets 2
Given an integer array nums that may contain duplicates, return all possible

subsets

(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example : 

nums = [1,3,3]

Output = [ [], [1], [3], [1,3], [3,3], [1,3,3] ]"""

def subset_with_dups(nums):
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
