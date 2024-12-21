def selection_sort(arr):
    
    n = len(arr)
    for i in range(n-1):
        min_ = i 
        for j in range(i+1, n):
            if arr[j] < arr[min_]:
                min_ = j 
        arr[i], arr[min_] = arr[min_], arr[i]
    return arr 
                
    # Your code goes here
    # minimum = 0 
    # swapped = False 
    # min_ = 0
    # for i in range(len(arr)):
    #     # smallest = arr[i]
    #     for j in range((i+1), len(arr)):
    #         if arr[j] < arr[i]:
    #             arr[i], arr[j] = arr[j], arr[i]
    #             continue
    # return arr
                
        

lst = [3, 5, 1, 2, 6]

print(selection_sort(lst))

"""Selection Sort
Selection Sort Algorithm

You are given a list of integers. Write a Python function to sort the list in ascending order using the Selection Sort algorithm. Selection Sort works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part.

Parameters:

lst (List of integers): The list to be sorted.

Returns:

A list of integers sorted in ascending order.

Example:

Input: lst = [64, 25, 12, 22, 11]
Output: [11, 12, 22, 25, 64]

Input: lst = [29, 10, 14, 37, 13]
Output: [10, 13, 14, 29, 37]"""