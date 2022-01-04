# You went to work and your husband stayed home today (because he is a bum: joy:)
# so you give him a list of chores to get done. Your list includes things like cleaning
# the bathroom and you decided to mark down that each chore takes a certain amount of time to do.
# Now because your husband is a bum he decides that he can only do a certain number of chores in
# the day because he needs his beauty sleep. You are very hardworking and love him so much that you
# decide to make it easier for him. Write some pseudo-code that does the following...
# take in 3 pieces of information

# 1. chores you want your husband to do
# 2. the total amount of sleep (in time) that your husband wants to have
# 3. the total amount of time your husband has to complete the chores

# return all the chores your husband can do and make sure that he does the most amount of chores from
# the list no matter what.

# (Note: your husband does not need to complete all chores but always needs to complete the most number of chores!)

# for example, if your husband wants to sleep 8 hours during the day but there are only 10 hours before you get back
# home he only has 2 hours to complete most of the chores. let's say you wrote down 10 chores for him to do and 2 of
# those chores add up to 2 hours but 8 of the other chores add up to 1 hour only. Then you should not return the 2
# chores your husband was able to do instead your husband should have been able to do the 9 chores so your return
# would look something like the following...

# [clean the patio, clean the stove, clean the fridge, clean the bathroom sink, vacuum the living room, make the bed,
# dust the window sills, do the laundry, fix the lights] where the total amount of time for all the chores added up to
# 2 hours only. let's say the last 2 chores both took 1 hour each. So that means 8 chores take 1 hour total and 1 chore
# takes 1 hour giving 2 hours total


# Example:
# Input
# Total time: 5hrs
# Sleep time: 3
# Chores time: 2hrs

# Chores & time;
# Cleaning: 30 minutes
# Laundry: 2hrs
# Shopping: 1hr
# Cooking: 30 minutes
# Taking out garbage: 30 minutes
# Making bed: 30minutes

# Output;
#  [Cleaning, Cooking, Taking out garbage, Making bed]


def possible_done_chores(chores, sleep_time, chores_time, total_time):

    chores_done = []
    chores_done_time = 0
    for chore in chores:
        # we sort the chores by the time required by each chore from the smallest to the largest
        chores.sort(key=lambda x: x[1])
        # we check if the time required by the chore is less than the time we have for chores
        if chore[1] <= (chores_time - chores_done_time):
            # if the time required by the chore is less than the time we have for chores we add the chore to the list
            # of chores done and we add the time required by the chore to the time we have for chores
            chores_done.append(chore[0])
            chores_done_time += chore[1]
        else:
            # if the time required by the chore is greater than the time we have for chores we break out of the loop
            # and return the list of chores done
            break

    return chores_done


chores = [
    ["Cleaning", 30],
    ["Laundry", 120],
    ["Shopping", 60],
    ["Cooking", 30],
    ["Taking out garbage", 30],
    ["Making bed", 30]
]


print(possible_done_chores(chores, 3, 120, 5))
