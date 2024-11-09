"""Coding Exercise: Monotonic Array
Question

An array is monotonic if it is either monotone increasing or monotone decreasing. 
An array is monotone increasing if all its elements from left to right 
are non-decreasing. An array is monotone decreasing if all  its elements 
from left to right are non-increasing. 
Given an integer array return true if the given array is 
monotonic, or false otherwise."""


def monotonic_array(array):
    n = len(array)
    if n == 0: return True 
    first = array[0]
    last = array[-1]
    
    if first < last:
        for k in range(n-1):
            if array[k] > array[k+1]:
                return False 
    elif first == last:
        for k in range(n-1):
            if array[k] != array[k+1]:
                return False 
    else:
        for k in range(n-1):
            if array[k] < array[k+1]:
                return False 
    
    return True 

inc = [1,2,3,4,5]
inc_broken = [1,2,-3,4,5]
same = [2,2,2,2,2]
same_broken = [2,2,3,2,2]
dec = [5,4,3,2,1]
dec_broken = [5,4,10,3,1]

lst = [inc, inc_broken, same, same_broken, dec, dec_broken]

for x in lst:
    print(f"{x} is monotonic?\n{monotonic_array(x)}")