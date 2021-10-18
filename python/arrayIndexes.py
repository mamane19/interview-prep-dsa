# Given an array of objects A, and an array of indexes B, reorder the objects in array A with the given indexes in array B.
# let a = [C, D, E, F, G, H];
# let b = [3, 0, 4, 1, 2, 5];

# $ reorder(a, b) // a is now [D, F, G, C, E, H]


def reorder(a, b):
    for i in range(len(b)):
        a[i], a[b[i]] = a[b[i]], a[i]
    return a


if __name__ == "__main__":
    a = ["C", "D", "E", "F", "G", "H"]
    b = [3, 0, 4, 1, 2, 5]
    print(reorder(a, b))
