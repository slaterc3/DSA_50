"""
T: O(n)
S: O(n) - recursive call stack
"""
def findTheWinner(n, k):
    # helper func
    def josephus(n):
        if n == 1: return 0 
        return (josephus(n-1) + k) % n 
    return josephus(n) + 1

if __name__ == "__main__":
    test_cases = [
        (1, 1, 1),
        (5, 2, 3),
        (7, 3, 4),
        (6, 6, 4),
        (4, 7, 2),
        (10, 3, 4)
    ]
    
    for i, (n, k, expected) in enumerate(test_cases, 1):
        result = findTheWinner(n, k)
        print(f"Test case {i}: n = {n}, k = {k}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"{'Passed' if result == expected else 'Failed'}\n")