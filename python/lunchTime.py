# This question is asked by Apple.
# You are serving people in a lunch line and need to ensure each person gets
# a “balanced” meal. A balanced meal is a meal where there exists the same number
# of food items as drink items. Someone is helping you prepare the meals and hands
# you food items (i.e. F) or a drink items (D) in the order specified by the items string.
# Return the maximum number of balanced meals you are able to create without being able to modify items.
# Note: items will only contain F and D characters.

# Ex: Given the following items…
# items = "FDFDFD", return 3
# the first "FD" creates the first balanced meal.
# the second "FD" creates the second balanced meal.
# the third "FD" creates the third balanced meal.

# Ex: Given the following items…
# items = "FDFFDFDD", return 2
# "FD" creates the first balanced meal.
# "FFDFDD" creates the second balanced meal.


def balanced_meals(items):
    """
    :param items: string of F and D characters
    :return: int of number of balanced meals

     >>> balanced_meals("FDFDFD")
     3
     >>> balanced_meals("FDFFDFDD")
     2
    """

    # Initialize variables
    balanced_meals = 0
    food_count = 0
    drink_count = 0

    # Loop through each character in items
    for char in items:
        if char == "F":
            food_count += 1
        elif char == "D":
            drink_count += 1

        # If food_count == drink_count, balanced_meals += 1
        if food_count == drink_count:
            balanced_meals += 1

    return balanced_meals


if __name__ == "__main__":
    print(balanced_meals("FDFDFD"))
    print(balanced_meals("FDFFDFDD"))
