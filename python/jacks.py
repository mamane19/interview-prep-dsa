
# Given a string of text, write a program that prints a list of unique words contained in the string
# along with the number of occurrences of each word in the string. The list should be sorted in
# descending order by frequency, and ascending order alphabetically when multiple words occur
# with the same frequency.
# For example, given the input:
# “This is a test. That is not a test. Test”
# The expected output could be: 
# {‘test’: 3, ‘is’: 2, ‘a’: 2, ‘that’: 1, ‘this’: 1}
# The output should be printed in a comma-separated list of words and their corresponding frequencies,
# sorted by frequency in descending order, and alphabetically in ascending order.
# For example, given the input:
# “This is a test. That is not a test. Test”
# The expected output could be:
# “test,3,a,2,is,2,not,1,that,1,this,1”

# *******************************
# Solution:
# *******************************


# define a function to get the list of words and their frequencies and sort it in descending order
# O(n) time and O(n) space
def get_sorted_list(text):
    # ignore the ponctuation in the text 
    text = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '')
    # ignore the uppercase and lowercase
    text = text.lower()
    # split the text into a list of words
    word_list = text.split()
    # initialize a dictionary to store the words and their frequencies
    word_freq = {}
    # loop through the word list
    for word in word_list:
        # if the word is not in the dictionary, add it with a frequency of 1
        if word not in word_freq:
            word_freq[word] = 1
        # if the word is already in the dictionary, increment its frequency by 1
        else:
            word_freq[word] += 1
    # sort the dictionary in descending order by frequency and in ascending order by alphabetical order
    word_freq = sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))
    # return the sorted list
    return word_freq


import string
# O(n) time and O(n) space
def words_freq_in_desc_order(text: str):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    words = text.split()
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    words_count = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))
    return words_count

if __name__ == '__main__':
    # Test the function
    text = "This is a test. That is not a test. Test"
    print(words_freq_in_desc_order(text))

