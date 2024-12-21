def binary_search(arr, target):
    if len(arr) == 0:
        return -1 
    start = 0 
    end = len(arr) -1 
    while (start <= end):
        mid = (end + start) // 2 
        if target == arr[mid]:
            return mid 
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1 

print(binary_search([1,2,3,4,5,6], 4))