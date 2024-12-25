
import math

class Solution:
  def shortestDistance(self, words, word1, word2):
    shortestDistance = len(words) # Initialize the shortest distance with the length of the words list
    position1, position2 = -1, -1 # Initialize the positions of word1 and word2 with -1
    for i, word in enumerate(words):
      if word == word1: # If the current word is word1, update the position1
        position1 = i
      elif word == word2: # If the current word is word2, update the position2
        position2 = i
      # If both the positions are updated, update the shortest distance
      if position1 != -1 and position2 != -1:
        shortestDistance = min(shortestDistance, abs(position1 - position2))

    return shortestDistance



# class Solution:
#   def shortestDistance(self, words, word1, word2):
#     # TODO: Write your code here
#     hash_m = {
#       word1: [],
#       word2: []
#     }
    
#     for i in range(len(words)):
#       if words[i] == word1:
#         hash_m[word1].append(i)
#       if words[i] == word2:
#         hash_m[word2].append(i)
    
#     min_dist = 300001
#     for i in range(len(hash_m[word1])):
#       for j in range(len(hash_m[word2])):
#         dist = abs(hash_m[word1][i] - hash_m[word2][j])
#         if dist < min_dist:
#           min_dist = dist 
    

#     return min_dist

if __name__ == "__main__":
  solution = Solution()

  # Test case 1
  words1 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
  word11 = "fox"
  word21 = "dog"
  expected_output1 = 5
  actual_output1 = solution.shortestDistance(words1, word11, word21)
  print("Test case 1:", expected_output1 == actual_output1)

  # Test case 2
  words2 = ["a", "b", "c", "d", "a", "b"]
  word12 = "a"
  word22 = "b"
  expected_output2 = 1
  actual_output2 = solution.shortestDistance(words2, word12, word22)
  print("Test case 2:", expected_output2 == actual_output2)

  # Test case 3
  words3 = ["a", "c", "d", "b", "a"]
  word13 = "a"
  word23 = "b"
  expected_output3 = 1
  actual_output3 = solution.shortestDistance(words3, word13, word23)
  print("Test case 3:", expected_output3 == actual_output3)

  # Test case 4
  words4 = ["a", "b", "c", "d", "e"]
  word14 = "a"
  word24 = "e"
  expected_output4 = 4
  actual_output4 = solution.shortestDistance(words4, word14, word24)
  print("Test case 4:", expected_output4 == actual_output4)  
"""Shortest Word Distance (easy)
Problem Statement
Given an array of strings words and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Example 1:

Input: words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], word1 = "fox", word2 = "dog"
Output: 5
Explanation: The distance between "fox" and "dog" is 5 words.
Example 2:

Input: words = ["a", "c", "d", "b", "a"], word1 = "a", word2 = "b"
Output: 1
Explanation: The shortest distance between "a" and "b" is 1 word. Please note that "a" appeared twice.
Example 3:

Input: words = ["a", "b", "c", "d", "e"], word1 = "a", word2 = "e"
Output: 4
Explanation: The distance between "a" and "e" is 4 words.
Constraints:

2 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
word1 and word2 are in words.
word1 != word2"""