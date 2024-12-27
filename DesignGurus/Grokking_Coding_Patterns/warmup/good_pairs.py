class Solution:
  def numGoodPairs(self, nums):
    pairCount = 0
    # TODO: Write your code here
    l = []
    for i in range(len(nums)-1):
      for j in range((i+1), len(nums)):
        if nums[i] == nums[j]:
          l.append((i,j))
    pairCount = len(l)
    return pairCount



"""Problem Statement
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs, here are the indices: (0,3), (0,4), (3,4), (2,5).
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array is a 'good pair'.
Example 3:

Input: words = nums = [1,2,3]
Output: 0
Explanation: No number is repeating.
Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100"""