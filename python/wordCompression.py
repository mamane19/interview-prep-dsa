# A student decides to perform some operations on big words to compress them,
# so they become easy to remember. An operation consists of choosing a group of
# k  consecutive equal characters and removing them. The student keeps performing this operation as long as it is possible.
# Determine the final word after the operation is performed.


# Input:
# word = "abbcccb"
# k = 3

# Output:
# 'a'


def compressWord(word, k):
    newWord = word
    while True:
        for i in range(len(word) - k + 1):
            if word[i] == word[i + k - 1]:
                newWord = newWord.replace(word[i:i + k], '')
                break
        if word == newWord:
            break
        word = newWord
    return word


if __name__ == '__main__':
    word = 'abbcccb'
    k = 3
    print(compressWord(word, k))
        
        
        
        
        
        
        # if len(word) > 1:
        #     for i in range(len(word) - k + 1):
        #         if word[i] == word[i + k - 1]:
        #             newWord = newWord.replace(word[i : i + k], "")
        #             word = newWord
        #             break
        # else:
        #     return word

        
    




