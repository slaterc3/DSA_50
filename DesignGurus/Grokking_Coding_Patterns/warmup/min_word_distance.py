
class Solution:
  def shortestDistance(self, words, word1, word2):
    # TODO: Write your code here
    hash_m = {
      word1: [],
      word2: []
    }
    
    for i in range(len(words)):
      if words[i] == word1:
        hash_m[word1].append(i)
      if words[i] == word2:
        hash_m[word2].append(i)
    
    min_dist = 300001
    for i in range(len(hash_m[word1])):
      for j in range(len(hash_m[word2])):
        dist = abs(hash_m[word1][i] - hash_m[word2][j])
        if dist < min_dist:
          min_dist = dist 
    

    return min_dist


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