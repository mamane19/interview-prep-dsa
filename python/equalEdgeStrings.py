# Given an array of strings words, for each consecutive pair of words check if they start and end with the same character.

# Return a boolean array of length words.length - 1, where ith element is true if words[i] and words[i + 1] start and end with the same character, and false otherwise.

# Example

# For words = ["abcd", "abdd", "da", "dd"], the output should be equalEdgedStrings(words) = [true, false, false].
# The first character of both words[0] and words[1] is 'a', and last one is - 'd'. So 0th element of the answer is true.
# The first character of words[1] is 'a', but the first character of words[2] is 'd'. So 1st element of the answer is false.
# The last character of words[2] is 'a', but the last character of words[3] is 'd'. So 2nd element of the answer is false.
# For words = ["a", "a"], the output should be equalEdgedStrings(words) = [true].
# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.string words

# An array of strings consisting of English lowercase letters.

# Guaranteed constraints:
# 1 ≤ words.length ≤ 100,
# 1 ≤ words[i].length ≤ 100.

# [output] array.boolean

# The array described in the problem statement.


def equalEdgedStrings(words):
     result = []
     for i in range(len(words)-1):
          if words[i][0] == words[i+1][0] and words[i][-1] == words[i+1][-1]:
               result.append(True)
          else:
               result.append(False)
     return result

