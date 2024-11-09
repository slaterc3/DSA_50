def sorted_array(array):
    n = len(array)
    if n <= 0:
        return 
    # making a new 
    new = [0] * n 
    for i in range(n):
        new[i] = array[i] ** 2 
    new.sort() 
    return new 

# Test cases
if __name__ == "__main__":
    # Define test cases
    test_cases = [
        ([-1, -2, 3, 5, 7], [1, 4, 9, 25, 49]),      # Mixed positive and negative
        ([0, -1, -3], [0, 1, 9]),                     # Mixed with zero
        ([3, 1, 2], [1, 4, 9]),                       # All positive
        ([], []),                                     # Empty list
        ([-4, -2, -5], [4, 16, 25]),                  # All negative
        ([0, 0, 0], [0, 0, 0]),                       # All zero
    ]
    
    # Run and print each test case result
    for i, (input_array, expected_output) in enumerate(test_cases, 1):
        result = sorted_array(input_array)
        print(f"Test case {i}: {input_array}")
        print(f"Expected: {expected_output}")
        print(f"Got: {result}")
        print(f"{'Passed' if result == expected_output else 'Failed'}\n")