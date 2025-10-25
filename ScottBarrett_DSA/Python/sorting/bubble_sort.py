def bubble_sort(l):
    n = len(l)
    swapped = False 
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j+1] < l[j]:
                l[j+1], l[j] = l[j], l[j+1]
                swapped = True 
        if not swapped:
            break 
    return l