class Solution:
  def findAverages(self, K, arr):
      result = []
      windowSum, windowStart = 0.0, 0
      for windowEnd in range(len(arr)):
          windowSum += arr[windowEnd]  # add the next element
          # slide the window, no need to slide if we've not hit the required window size of 'k'
          if windowEnd >= K - 1:
              result.append(windowSum / K)  # calculate the average
              windowSum -= arr[windowStart]  # subtract the element going out
              windowStart += 1  # slide the window ahead

      return result


def main():
  sol = Solution()
  result = sol.findAverages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()


# naive solution
# class Solution:
#   def findAverages(self, K, arr):
#     result = []
#     for i in range(len(arr)-K+1):
#       # find sum of next 'K' elements
#       _sum = 0.0
#       for j in range(i, i+K):
#         _sum += arr[j]
#       result.append(_sum/K)  # calculate average

#     return result


# def main():
#   sol = Solution()
#   result = sol.findAverages(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
#   print("Averages of subarrays of size K: " + str(result))


# main()