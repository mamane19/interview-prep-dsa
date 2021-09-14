# You are given a sring s containing lowercase English letters.
# you should check if there are three adjascent letters that are not the same.
# If so, you count the number of such triplets and return it.
# If there are no such triplets, return 0.


def check_triplets(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i] != s[i + 1] and s[i] != s[i + 2] and s[i + 1] != s[i + 2]:
            count += 1
    return count

if __name__ == '__main__':
    print(check_triplets('abbca'))
    print(check_triplets('abccb'))
    print(check_triplets('abcdd'))