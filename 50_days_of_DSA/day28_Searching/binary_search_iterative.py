# T: O(log n)
# S: O(1) - constant space for iterative solution, O(log n) if recursive

def binary_search(arr, target):
    left = 0 
    right = len(arr) - 1 
    while left <= right:
        middle = (left + right) // 2 
        if arr[middle] == target:
            return middle 
        elif arr[middle] > target:
            right = middle - 1 
        else:
            left = middle + 1 
    return -1 

print(binary_search([1,2,3,4,5,6,7,8,9], 9))