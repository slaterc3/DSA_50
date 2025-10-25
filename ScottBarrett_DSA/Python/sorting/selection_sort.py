## WRITE SELECTION_SORT FUNCTION HERE ##
#                                      #
#                                      #

def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        min_idx = i 
        for j in range(i+1, n):
            if l[j] < l[min_idx]:
                min_idx = j 
        if i != min_idx:
            l[min_idx], l[i] = l[i], l[min_idx]
    return l


######################################## 




print(selection_sort([4,2,6,5,1,3]))


 
"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

