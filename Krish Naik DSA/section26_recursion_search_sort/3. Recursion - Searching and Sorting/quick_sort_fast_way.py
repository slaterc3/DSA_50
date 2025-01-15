def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    
    # get the pivot
    pivot = arr[-1]
        
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    return quick_sort(left) + pivot + quick_sort(right)

print(quick_sort([5,4,3,2,1]))