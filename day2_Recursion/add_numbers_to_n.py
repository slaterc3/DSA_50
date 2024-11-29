# adding all non-negative numbers up to n

def add_n(n):

    if n < 0: 
        return 0 
    return n + add_n(n-1)

if __name__ == "__main__":
    test_cases = [
        (1, 1),
        (0, 0),
        (4, 10),
        (5, 15)
    ]
    for i, (n, expected) in enumerate(test_cases, 1):
        result = add_n(n)
        print(f"Test case {i}: n = {n}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"{'Passed' if result == expected else 'Failed'}\n")