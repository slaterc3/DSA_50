# iteration 
# as we know the answer of n=1 -> 0 (+1) is the safe 
# we can keep iterating through
# using the same formula as before:
# (safe + k) % n 
# prev starts as 0, and then updates
# size of n updates, but k remains 

def josephus_problem(n, k):
    """
    Time: O(n), Space: O(1)
    """
    # we know for n==1, answer is 0, so start at 2
    safe = 0
    for i in range(2, n+1):
        safe = (safe + k) % i
    
    return safe + 1 
   
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
        result = josephus_problem(n, k)
        print(f"Test case {i}: n = {n}, k = {k}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"{'Passed' if result == expected else 'Failed'}\n")     

