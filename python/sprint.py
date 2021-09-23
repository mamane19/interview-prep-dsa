# Pat is an ordinary kid who works hard to be a great runner. 
# As part of training, Pat must run sprints of different intervals on a straight trail.  
# The trail has numbered markers that the coach uses as goals.  Pat's coach provides a list of goals to reach in order.  
# Each time Pat starts at, stops at, or passes a marker it is considered a visit.
# Determine the lowest numbered marker that is visited the most times during Pat's day of training.  

# example:
# n = 5
# sprints = [2, 4, 1, 3]
# if the number of markers on the trail, n, is 5, and the list of sprints is [2, 4, 1, 3], 
# pat first sprints from position  2 --> 4. The next sprint starts at 4 and stops at 1.
# and then 1 --> 3.
# A marker numbered position p is considered to be visited each time Pat either starts or ends a sprint 
# there and each time it is passed while sprinting. The total number of visits to each position in the example 
# is calculated.
# Pat has visited markers 2 and 3 a total of 3 times each. Since 2 < 3,
# the lowest numbered marker that is visited the most times during Pat's day of training is 2. 


def getMostVisitedMarker(n, sprints):
     visited = [0] * (n + 1)
     for i in range(len(sprints) - 1):
          if sprints[i] < sprints[i + 1]:
               visited[sprints[i]] += 1
               visited[sprints[i + 1]] += 1
          else:
               visited[sprints[i + 1]] += 1
               visited[sprints[i]] += 1
     return visited.index(max(visited))