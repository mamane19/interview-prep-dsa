# A string is said to be a k-interspace string if the absolute difference of the
# ASCII values of every pair of adjacent characters is at most k. For example - "abac" is a k-interspace
# string for k ≥ 2 since the absolute difference between every adjacent character of it is at most 2.
# A substring is any group of contiguous characters in a string. For example, the substrings of
# abc = [abc, ab, bc, a, b, c]. A substring of a string is said to be k-interspace substring
# if the substring is a k-interspace string.

# Given a string, word, and an integer, k, find the longest k-interspace substring within word.
# If there are multiple substrings of the longest length, return the one that occurs first in word.


def dist(a, b):
    return abs(ord(a)-ord(b))


def longestKInterspaceSubstring(word, k):
    temp = ""
    maxi = ""
    flag = 0
    for i in range(len(word) - 1):
        temp += word[i]
        if dist(word[i], word[i + 1]) > k:
            flag = 1
            if len(maxi) >= len(temp):
                maxi = maxi
            else:
                maxi = temp

            temp = ""

        if i == len(word) - 2:
            temp += word[i + 1]

    if flag == 0:
        maxi = temp

    return maxi
