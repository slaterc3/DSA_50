# T: O(log n), S: O(log n)
def binary_search(arr, target):
    def helper(arr, target, start, end):
        if start > end:
            return -1 
        mid = (start + end) // 2 
        if target == arr[mid]:
            return mid 
        elif target < arr[mid]:
            return helper(arr, target, start, mid-1)
        else:
            return helper(arr, target, mid+1, end)
    return helper(arr, target, start=0, end=len(arr)-1)

print(binary_search([1,2,3,4,5,6,7,8], 8))
print(binary_search([1,2,3,4,5,6,7,8], 9))