def search_for_range(array, target):
    
    def find_left_extreme(array, target):
        left = 0
        right = len(array) - 1 
        while left <= right:
            mid = (left + right)//2 
            if target == array[mid]:
                if mid == 0:
                    return mid 
                elif array[mid-1] == target:
                    right = mid-1 
                else:
                    return mid 
            elif target < array[mid]:
                right = mid - 1 
            else:
                left = mid + 1 
        return -1 
    
    def find_right_extreme(array, target):
        left = 0
        right = len(array)-1 
        while left <= right:
            mid = (left+right)//2 
            if target == array[mid]:
                if mid == 0:
                    return mid 
                elif array[mid+1] == target:
                    left = mid + 1 
                else:
                    return mid 
            else:
                if target > array[mid]:
                    left = mid + 1 
                else:
                    right = mid - 1 
        return -1 
    left = find_left_extreme(array, target)
    right = find_right_extreme(array, target)
    return [left, right]
print(search_for_range([1,2,2,2,3,4], 2))