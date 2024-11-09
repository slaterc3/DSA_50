"""Coding Exercise: Monotonic Array
Question

An array is monotonic if it is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right 
are non-decreasing. An array is monotone decreasing if all  its elements 
from left to right are non-increasing. 
Given an integer array return true if the given array is 
monotonic, or false otherwise."""


def monotonic_array(array):
    n = len(array)
    if n == 0: return True 
    # to check first and last elements
    first = array[0]
    last = array[-1]
    
    # if monotonic increasing
    if first < last:
        for k in range(n-1):
            if array[k] > array[k+1]:
                return False 
    elif first == last:
        for k in range(n-1):
            if array[k] != array[k+1]:
                return False 
    else: # if monotonic decreasing
        for k in range(n-1):
            if array[k] < array[k+1]:
                return False 
    
    return True 

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], True),
        ([3, 3, 3, 3], True),
        ([1, 3, 2, 4, 5], False),
        ([2, 2, 3, 4], True),
        ([5, 4, 4, 3, 2], True),
        ([1], True),
        ([], True),
        ([3, 3, 2, 1, 4], False)
    ]

    for i, (array, expected) in enumerate(test_cases, 1):
        result = monotonic_array(array)
        print(f"Test case {i}: {array}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"{'Passed' if result == expected else 'Failed'}\n")
    