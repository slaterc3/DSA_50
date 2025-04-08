def combinationsSum(candidates, target):
    res = [] # what we will return
    n = len(candidates)
    
    def helper(start_idx=0, curr=[], sum_incl=0):
        # base case(s)
        if sum_incl > target:
            return 
        if sum_incl == target:
            res.append(curr[:])
            return 
        for j in range(start_idx, n):
            curr.append(candidates[j])
            helper(j, curr, sum_incl+candidates[j])
            curr.pop()
    helper(0, [], 0)
    return res 

if __name__ == "__main__":
    test_cases = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),  # Basic test case with unique combinations
        ([2, 3, 5], 8, [[2, 2, 2, 2],  [2, 3, 3], [3, 5]]),  # Multiple ways to form the target
        ([2], 1, []),  # No combinations possible
        ([1], 2, [[1, 1]]),  # Only one candidate
        ([2, 3, 6, 7], 9, [[2, 2, 2, 3],[2, 7], [3, 3, 3], [3,6]]),  # Target larger than individual candidates
        ([1, 2], 4, [[1, 1, 1, 1], [1, 1, 2], [2, 2]]),  # Small numbers and simple combinations
        ([2, 4, 6], 8, [[2, 2, 2, 2], [2, 2, 4], [2,6], [4, 4]]),  # Even numbers only
    ]

    for i, (candidates, target, expected) in enumerate(test_cases, 1):
        result = combinationsSum(candidates, target)
        print(f"Test case {i}: candidates = {candidates}, target = {target}")
        print(f"Expected: {sorted(expected)}")
        print(f"Got: {sorted(result)}")
        print(f"{'Passed' if sorted(result) == sorted(expected) else 'Failed'}\n") 
        
        
