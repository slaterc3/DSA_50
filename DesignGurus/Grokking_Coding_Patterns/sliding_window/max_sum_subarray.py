class Solution:
  def findMaxSumSubArray(self,k, arr):
    # TODO: Write your code here
    if len(arr) == 0: return -1
    res = []
    start, total = 0,0
    for end in range(len(arr)):
      total += arr[end]
      if end >= k-1:
        res.append(total)
        total -= arr[start]
        start += 1 
    return max(res)
    