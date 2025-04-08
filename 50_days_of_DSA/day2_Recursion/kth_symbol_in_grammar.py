"""Coding Exercise (k-th symbol in Grammar)
We build a table of n rows (1-indexed). 
We start by writing 0 in the 1st row. 
Now in every subsequent row, we look at the 
previous row and replace each occurrence of 0 with 01, 
and each occurrence of 1 with 10. 
For example, for n = 3, 
the 1st row is 0, 
the 2nd row is 01, 
and the 3rd row is 0110. 
Given two integer n and k, 
return the kth (1-indexed) symbol 
in the nth row of a table of n rows."""

def kth_symbol(n, k):
    # base case
    if n == 1:
        return 0 
    L = 2 ** (n-1) # gives us length of array
    mid = L // 2 # gives midpoint
    
    if k <= mid:
        return kth_symbol(n-1, k)
    else:
        return int(not(kth_symbol(n-1, k-mid)))

if __name__ == "__main__":
    test_cases = [
        (1, 0, 0),
        (2, 1, 1),
        (3, 2, 1),
        (3, 3, 0),
        (4, 4, 1),
        (4, 7, 1),
        (5, 10, 0),
        (6, 31, 0)
    ]

    for i, (n, k, expected) in enumerate(test_cases, 1):
        result = kth_symbol(n, k)
        print(f"Test case {i}: n = {n}, k = {k}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"{'Passed' if result == expected else 'Failed'}\n")
    