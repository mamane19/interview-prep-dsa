# A Supply Chain Manager at an Amazon warehouse is reviewing the logs of when 
# trucks arrived at and departed from their warehouse. Please help them with their 
# review by completing the following challenge: Given a collection of time intervals, [start, end],
# merge and return the overlapping intervals sorted in ascending order of their start times.

#for example:
# intervals = [[7,7],[2,3],[6,11],[1,2]]
# output = [[1, 3], [6, 11]]


def mergedInterval(intervals):
     intervals.sort(key=lambda x: x[0])
     merged = []
     for interval in intervals:
          if not merged or merged[-1][1] < interval[0]:
               merged.append(interval)
          else:
               merged[-1][1] = max(merged[-1][1], interval[1])
     return merged


intervals = [[7,7],[2,3],[6,11],[1,2]]
print(mergedInterval(intervals))


