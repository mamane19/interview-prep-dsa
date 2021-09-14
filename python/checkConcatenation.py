# You are given two arrays of strings, A and B.
# Check if there is a string in array B which is a conatenation of some of the strings in array A.
# if there is, return true, else return false.
# For example,
# A = ["one", "two", "three"]
# B = ["one", "onetwo", "four"] => return true
# B = ["one", "two", "three", "four"] => return false
# B = ["one", "two", "three", "four", "five"] => return false


def check_concatenation(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j:j+i+1]:
                return True
    return False

if __name__ == "__main__":
    a = ["one", "two", "three"]
    b = ["one", "onetwo", "four"]
    print(check_concatenation(a, b))