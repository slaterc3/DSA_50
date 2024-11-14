def permute(nums):
    n = len(nums)
    ans, sol = [], []
    
    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            return 
        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop() #backtracking part 
        
    backtrack()
    return ans 

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
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