# Camel Case Machine
# Programming challenge description:
# Reformat a series of strings into Camel Case by returning the fragments from input as a single "sentence". For example, consider the following input:

# Camel 
# Case
 
# LOOKS
# like
# ThIs
# Would result in:

# camelCase looksLikeThis
# Input:
# A series of strings with one fragment on each line of input. All characters will be from the ASCII character set.

# Output:
# A single line with the inputs assembled in Camel Case

# Test 1
# Test Input
# Download Test 1 Input
# Apple
# One
 
# Apple
# TWO
 
# APPLE
# three
# Expected Output
# Download Test 1 Input
# appleOne appleTwo appleThree
# Test 2
# Test Input
# Download Test 2 Input
# MERCURY
 
# VENUS
 
# EARTH
 
# MARS
 
# GIANTS
# JUPITER
# SATURN
# URANUS
# NEPTUNE
 
# PLUTO
# Expected Output
# Download Test 2 Input
# mercury venus earth mars giantsJupiterSaturnUranusNeptune pluto
# Test 3
# Test Input
# Download Test 3 Input
# the
# dog
# jumped
# over
# the
# lazy
# moon
# Expected Output
# Download Test 3 Input
# theDogJumpedOverTheLazyMoon

import sys 
for line in sys.stdin: 
     words = line.split(" ") 
     s = "".join(word[0])
     for word in words:
          print(s.upper() + "".join(word[1:]))