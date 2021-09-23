# A music player allows users to choose songs to play, but only in pairs and only pairs of songs with durations that add up to a multiple of 60 seconds 
# (e.g., 60, 120, 180). Given a list of song durations, calculate the total number of different song pairs that can be chosen.

# songs = [20, 40, 60]
# One pair of songs can be chosen whose combined duration is a multiple of a whole minute (20 + 40 = 60).
# and the return value would be 1. While the third song is a single minute long, songs must be chosen in pairs.

import collections
def playlist(songs):
     seen = collections.Counter()
     count = 0
     for song in songs:
          count += seen[-song%60]
          seen[song % 60] += 1
     return count