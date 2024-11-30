"""Coding Exercise: Combinations Sum 2
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations."""

def combos_sum2(candidates, target):
    # sort candidates, hash map needed
    candidates.sort()
    res = []
    n = len(candidates)
    
    def helper(idx, curr, curr_sum):
        # base case(s)
        if curr_sum == target:
            res.append(curr[:])
            return 
        if curr_sum > target:
            return 
        if idx > n-1:
            return 
        # end base cases 
        hash_map = {}
        for i in range(idx, n):
            if candidates[i] not in hash_map:
                hash_map[candidates[i]] = 1 
                curr.append(candidates[i])
                helper(i+1, curr, curr_sum + candidates[i])
                curr.pop() 
                
    helper(0, [], 0)
    return res 

print(combos_sum2([2,3,4,3,5], 8))