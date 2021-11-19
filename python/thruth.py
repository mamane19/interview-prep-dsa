# Write a programme that takes as input 2 finite sets or lists (you decide) X and Y , where X, Y ⊂ Z,
# and outputs a truth value (’True’ or ’False’) for the following statement:
# ∀x ∈ X, ∃y ∈ Y such that y | x.



#     print(thruth(x, y, z))


def thruth(x, y):
    for i in x:
        for j in y:
            if i % j == 0:
                return True
    return False


if __name__ == '__main__':
    x = [1, 2, 3]
    y = [4, 5, 6]
#     z = [7, 8, 9]
    print(thruth(x, y))
