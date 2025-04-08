def search_rotated_sorted_array(nums, target):
    #write your code here
    # for i in range(len(nums)):
    #     if target == nums[i]:
    #         return i 
    # return -1
    left = 0 
    right = len(nums)-1 
    while left <= right:
        mid = (left+right)//2 
        if target == nums[mid]:
            return mid 
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1 
            else:
                 left = mid + 1 
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1 
            else:
                right = mid -1 
    return -1 
            


"""Coding Exercise: Search in rotated sorted array
Question:

Search in Rotated Sorted array- You are given an integer array nums sorted in ascending order (with distinct values). Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).  For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2]. Given an integer target, return the index of target if it is in the array, else return -1. You must write an algorithm with O(log n) runtime complexity."""