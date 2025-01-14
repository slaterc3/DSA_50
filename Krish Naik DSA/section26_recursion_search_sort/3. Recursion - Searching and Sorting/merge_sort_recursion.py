def merge_sort(arr):
    """
    Function to perform merge sort on a list of integers using recursion.
    
    Parameters:
    arr (list of int): The list to be sorted.
    
    Returns:
    list of int: The sorted list.
    """
    # Your code here
    def merge(l, r):
        ans = []
        i = 0
        j = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                ans.append(l[i])
                i += 1 
            elif l[i] > r[j]:
                ans.append(r[j])
                j += 1 
            else:
                ans.append(l[i])
                ans.append(r[j])
                i += 1 
                j += 1 
        
        if i < len(l):
            ans.extend(l[i:])
        if j < len(r):
            ans.extend(r[j:])
        return ans 
    
    if len(arr) <= 1:
        return arr 
    
    m = len(arr) // 2 
    
    l = arr[:m]
    r = arr[m:]
    
    sorted_l = merge_sort(l)
    sorted_r = merge_sort(r)
    
    return merge(sorted_l, sorted_r)
    

print(merge_sort([1,3,2,4]))
print(merge_sort([5,4,3,2,1]))



