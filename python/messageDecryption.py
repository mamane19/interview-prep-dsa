# This question is asked by Microsoft. Given a message that is encoded using the following encryption method…

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# Return the total number of ways it can be decoded.
# Note: ‘0’ has no mapping and a character following a ‘0’ also has no mapping (i.e. “03”)


# Ex: Given the following message…

# message = "23", return 2.
# The message can be decrypted as "BC" (i.e. 2 -> B, 3 -> C)
# The message can also be decrypted as "W" (i.e. 23 -> W)
# Ex: Given the following message…

# message = "1234", return 3.


def messageDecryption(message):
    # Write your code here
    # return 0
    if len(message) == 1:
        return 1
    elif len(message) == 2:
        if int(message) <= 26:
            return 2
        else:
            return 1
    else:
        if int(message[:2]) <= 26:
            return messageDecryption(message[1:]) + messageDecryption(message[2:])
        else:
            return messageDecryption(message[1:])


print(messageDecryption("1234"))
print(messageDecryption("23"))
