"""Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example: n = 4, k=2
Output =

[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]"""

def combinations(n, k):
    res = [] 
    def helper(start, curr):
        if len(curr) == k:
            res.append(curr[:])
            return 
        need = k - len(curr)
        for j in range(start, n-(need-1)+1):
            curr.append(j)
            helper(j+1, curr)
            curr.pop() 
    helper(1, [])
    return res 

if __name__ == "__main__":
    # Test cases
    test_cases = [
        (4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
        (5, 3, [
            [1, 2, 3], [1, 2, 4], [1, 2, 5],
            [1, 3, 4], [1, 3, 5], [1, 4, 5],
            [2, 3, 4], [2, 3, 5], [2, 4, 5],
            [3, 4, 5]
        ]),
        (3, 2, [[1, 2], [1, 3], [2, 3]]),
        (3, 3, [[1, 2, 3]]),
        (4, 1, [[1], [2], [3], [4]]),
        (1, 1, [[1]]),
        (4, 4, [[1, 2, 3, 4]]),
    ]

    for i, (n, k, expected) in enumerate(test_cases, 1):
        result = combinations(n, k)
        print(f"Test case {i}: n = {n}, k = {k}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"{'Passed' if sorted(result) == sorted(expected) else 'Failed'}\n")