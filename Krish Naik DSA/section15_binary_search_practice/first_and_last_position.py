def searchRange(nums, target):
    """
    Find the starting and ending position of a given target value in a sorted array.
    Use binary search to find both the first and last occurrence of the target.
    """
    def findFirst(nums, target):
        """
        Find the first occurrence of the target using binary search.
        """
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            print(f'findFirst: left: {left}, right: {right}')
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
 
    def findLast(nums, target):
        """
        Find the last occurrence of the target using binary search.
        """
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            print(f'findLast: left: {left}, right: {right}')
            mid = (left + right) // 2
            if nums[mid] == target:
                # print(f'nums[mid]==target: {left)
                result = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result
 
    start = findFirst(nums, target)
    end = findLast(nums, target)
 
    return [start, end]

# first attempt:
# def searchRange(nums, target):
#     # Implement your solution here
#     left = 0 
#     right = len(nums) -1 
#     lower = -1 
#     upper = -1
#     while left <= right:
#         mid = (left + right) // 2 
#         if target == nums[mid]:
#             upper = mid 
#             lower = mid 
#             while upper < (len(nums)-1) and target == nums[upper+1]:
#                 print(f'upper: {upper}')
#                 upper += 1 
 
#             while lower > 0 and target == nums[lower - 1]:
#                 print(f'lower: {lower}')
#                 lower -= 1 
#             return [lower, upper]
#         elif target < nums[mid]:
#             right = mid - 1 
#         else: 
#             left = mid + 1 
#     return [lower, upper]
    

print(searchRange([1,2,3,3,4,5,6,7,7,7], 7))


"""Find First and Last Position of Element in Sorted Array
Asked in companies

Goldman sachs

Amazon

Wipro

Airtel



Description:
Given an array of integers nums sorted in non-decreasing order, and an integer target, find the starting and ending position of the given target value. If target is not found in the array, return [-1, -1].



Parameters:

nums (List[int]): A list of integers sorted in non-decreasing order.

target (int): The target value to search for.

Return Values:

List[int]: The starting and ending positions of the target value in the array. If the target is not found, return [-1, -1].



Example:

Input: nums = [5, 7, 7, 8, 8, 10], target = 8 
Output: [3, 4] 
Explanation: The target 8 appears from index 3 to index 4.
 
 
Input: nums = [5, 7, 7, 8, 8, 10], target = 6 
Output: [-1, -1] 
Explanation: The target 6 is not found in the array."""