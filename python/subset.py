# given two lists of numbers, check if the second list is a subset of the first list.
# They do not have to be with the same length. If the second list is also empty, return True.


def subset(list1, list2):
    if len(list2) == 0:
        return True
    for i in list2:
        if i not in list1:
            return False
    return True
