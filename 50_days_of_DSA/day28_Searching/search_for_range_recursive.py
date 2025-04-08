def find_extreme_left(arr, target, range, left, right):
    if left > right: 
        return 
    mid = (left + right) // 2 
    if arr[mid] == target:
        if mid == 0: 
            range[0] = 0 
        elif arr[mid-1] == target:
            find_extreme_left(arr, target, range, left, mid-1)
        else:
            range[0] = mid 
    elif target < arr[mid]:
        find_extreme_left(arr, target, range, left, mid-1)
    else:
        find_extreme_left(arr, target, range, mid+1, right)
        
def find_extreme_right(arr, target, range, left, right):
    if left > right: return 
    mid = (left+right)//2 
    if target == arr[mid]:
        if mid == len(arr) - 1:
            range[1] = len(arr)-1 
        elif arr[mid+1] == target:
            find_extreme_right(arr, target, range, mid+1, right)
        else:
            range[1] = mid 
    elif target > arr[mid]:
        find_extreme_right(arr, target, range, mid+1, right)
    else:
        find_extreme_right(arr, target, range, left, mid-1)
        
def search_for_range(arr, target):
    range = [-1, -1]
    find_extreme_left(arr, target, range, 0, len(arr)-1)
    find_extreme_right(arr, target, range, 0, len(arr)-1)
    return range

print(search_for_range([1,2,2,2,3,4], 2))