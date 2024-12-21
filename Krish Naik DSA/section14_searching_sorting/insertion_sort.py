def insertion_sort(arr):
    # Your code goes here
    # improved
    n = len(arr)
    for i in range(1, n):
        curr = arr[i]
        j = i - 1 
        while j >= 0:
            if arr[j] < curr:
                break 
            else:
                arr[j+1] = arr[j] 
                j -= 1 
        arr[j+1] = curr 
    return arr 
    # swap = False 
    # n = len(arr)
    # for i in range(1, n):
    #     curr = i 
    #     current_value = arr[curr]
    #     prev = i - 1 
    #     prev_value = arr[prev]
    #     while arr[curr] < arr[prev] and prev >= 0:
    #         # if arr[curr] < arr[prev]:
    #         arr[curr], arr[prev] = arr[prev], arr[curr]
    #         curr -= 1 
    #         prev -= 1 
    #         # else:
    #         #     swap = False 
    # return arr 
    
print(insertion_sort([12,11,13,5,6]))

"""Insertion Sort
Insertion Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Insertion Sort algorithm. Insertion Sort works by building a sorted section of the list, one element at a time, by inserting each new element into its proper position within the already sorted section.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.

Example:

Input: lst = [12, 11, 13, 5, 6]
Output: [5, 6, 11, 12, 13]

Input: lst = [31, 41, 59, 26, 41, 58]
Output: [26, 31, 41, 41, 58, 59]"""