class Solution:
  def makeSquares(self, arr):
    n = len(arr)
    squares = [0 for x in range(n)]
    # TODO: Write your code here
    i = 0 
    j = len(arr) - 1 
    ctr = -1 
    while i <= j:
      if abs(arr[i]) > abs(arr[j]):
        squares[ctr] = arr[i] ** 2 
        i += 1 
      else:
        squares[ctr] = arr[j] ** 2 
        j -= 1 
      ctr -= 1 
    return squares


"""
Problem Statement
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
Constraints:

1 <= arr.length <= 104
-104 <= arr[i] <= 104
arr is sorted in non-decreasing order."""