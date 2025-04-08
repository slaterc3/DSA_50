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

if __name__ == "__main__":
    test_cases = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
        ([1, 1, 1, 2, 2], 4, [[1, 1, 2], [2, 2]]),
        ([3, 1, 3, 5, 1], 8, [[1, 1, 3, 3], [3, 5]]),
        ([2, 3, 6, 7], 7, [[7]]),  # Single combination
        ([2, 2, 2], 4, [[2, 2]]),  # Avoid duplicates
        ([1, 2, 3], 10, []),  # Target too large
        ([], 5, []),  # No candidates
    ]

    for i, (candidates, target, expected) in enumerate(test_cases, 1):
        result = combos_sum2(candidates, target)
        print(f"Test case {i}: candidates = {candidates}, target = {target}")
        print(f"Expected: {sorted(expected)}")
        print(f"Got: {sorted(result)}")
        print(f"{'Passed' if sorted(result) == sorted(expected) else 'Failed'}\n")