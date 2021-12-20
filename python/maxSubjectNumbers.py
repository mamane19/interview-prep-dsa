# Your team at Amazon is building a quiz-style application to help students prepare for certification exams. 
# Each quiz module tests one or more subjects and limits the number of answers students can provide. 
# You have been asked to examine the impact of this limit on the ability of students to "pass" certain subjects within quiz modules. 
# To do this, please review and solve for the following: 
# Imagine a student has already answered answered[i] questions on the ith subject, and 
# still has to answer a total of q more questions overall.
# For each ith  subject, the number of questions answered has to be at least needed[i] to pass the subject.
# Determine the maximum number of subjects the student can pass if the q  additional answered questions are optimally distributed among the subjects.

# sample input: [3, 24, 27, 0, 3, 51, 52, 100, 100]
# answered = [24, 27, 0]
# needed = [27, 25, 100]
# The best distribution is at least 27 + 25 = 52 questions on the first two subjects. It will
# take all q = 100 questions to pass the third subject.
# sample output:
# 2


# sample input:[3, 24, 27, 0, 3, 51, 52, 100, 100]
# answered = [24, 27, 0, 3, 51, 52, 100, 100]
# needed = [27, 25, 100, 100]
# The best distribution is at least 27 + 25 = 52 questions on the first two subjects. It will
# take all q = 100 questions to pass the third subject.
# sample output:
# 3


# def maxSubjectsNumber(answered, needed, q):





