# class Solution:
#   vowels = "aeiouAEIOU"
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Use a set for faster lookup
        s = list(s)  # Convert string to a list to modify it
        left, right = 0, len(s) - 1  # Initialize two pointers

        while left < right:
            # Move `left` pointer until a vowel is found
            while left < right and s[left] not in vowels:
                left += 1
            # Move `right` pointer until a vowel is found
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap the vowels at `left` and `right`
            s[left], s[right] = s[right], s[left]

            # Move the pointers closer
            left += 1
            right -= 1

        return ''.join(s)  # Convert list back to a string
#   def reverseVowels(self, s: str) -> str:
#     # initialize pointers for start and end of the string
#     first, last = 0, len(s) - 1
#     array = list(s)
#     while first < last:
#       # increment the start pointer until a vowel is found
#       while first < last and self.vowels.find(array[first]) == -1:
#         first += 1
#       # decrement the end pointer until a vowel is found
#       while first < last and self.vowels.find(array[last]) == -1:
#         last -= 1
#       # swap the values of first and last if both are vowels
#       array[first], array[last] = array[last], array[first]
#       # move the pointers towards the center
#       first += 1
#       last -= 1

#     # return the modified string
#     return "".join(array)
    

if __name__ == "__main__":
  solution = Solution()

  s1 = "hello"
  expected_output1 = "holle"
  actual_output1 = solution.reverseVowels(s1)
  print("Test Case 1: ", expected_output1 == actual_output1)

  s2 = "DesignGUrus"
  expected_output2 = "DusUgnGires"
  actual_output2 = solution.reverseVowels(s2)
  print("Test Case 2: ", expected_output2 == actual_output2)

  s3 = "AEIOU"
  expected_output3 = "UOIEA"
  actual_output3 = solution.reverseVowels(s3)
  print("Test Case 3: ", expected_output3 == actual_output3)

  s4 = "aA"
  expected_output4 = "Aa"
  actual_output4 = solution.reverseVowels(s4)
  print("Test Case 4: ", expected_output4 == actual_output4)

  s5 = ""
  expected_output5 = ""
  actual_output5 = solution.reverseVowels(s5)
  print("Test Case 5: ", expected_output5 == actual_output5)

"""
class Solution:
  def reverseVowels(self, s: str) -> str:
    # TODO: Write your code here

    vowels = 'aeiouAEIOU'
    v = []
    s = list(s)
    for i in range(len(s)):
      if s[i] in vowels:
        
        v.append(s[i])
        s[i] = '*'

    for j in range(len(s)):
      if s[j] == '*':
        print(v)
        s[j] = v.pop()
    
    return ''.join(s)
"""