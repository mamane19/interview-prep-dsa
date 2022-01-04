# Given a positive number, return its complementary number.
# Note: The complement of a number is the number that results from flipping every bit in the original number.
# (i.e. zero bits become one bits and one bits become zero bits).

# Ex: Given the following number…
# number = 27, return 4.
# 27 in binary (not zero extended) is 11011.
# Therefore, the complementary binary is 00100 which is 4.


def find_complement(number):
    binary = bin(number)
    binary = binary[2:]
#     print(binary) # 11011 -> 00100 -> 4, so return 4 for 27. 
    complement = ''
    for i in binary:
        if i == '0':
            complement += '1'
        else:
            complement += '0'
    return int(complement, 2)


print(find_complement(27))
print(find_complement(5))