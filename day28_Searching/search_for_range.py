def search_for_range(array,target):
    #write your code here
    def find_first(array, target):
        l = 0 
        r = len(array)-1 
        res = -1 
        while l <= r:
            m = (l+r) // 2 
            if target == array[m]:
                res = m 
                r = m - 1 
            elif target < array[m]:
                r = m - 1 
            else:
                l = m + 1 
        return res 
    
    def find_last(array, target):
        l = 0 
        r = len(array) - 1 
        res = -1 
        while l <= r:
            m = (l+r) // 2 
            if target == array[m]:
                res = m 
                l = m + 1 
            elif target < array[m]:
                r = m - 1 
            else:
                l = m  + 1 
        return res 
        
    first = find_first(array, target)
    last = find_last(array, target)
    
    return [first, last]
    

print(search_for_range([1,2,2,2,3,4], 2))

"""Coding Exercise: Search for range
Question:

Find First and Last Position of Element in Sorted Array-You are given an array of integers sorted in non-decreasing order, find the starting and ending position of a given target value. If target is not found in the array, return [-1, -1]. You must write an algorithm with O(log n) runtime complexity.

Try:

Try to write both the iterative solution and recursive solution"""