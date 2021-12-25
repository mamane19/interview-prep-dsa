# A frog is attempting to cross a river to reach the other side. 
# Within the river, there are stones located at different positions 
# given by a stones array (this array is in sorted order). Starting 
# on the first stone (i.e. stones[0]), the frog makes a jump of size 
# one potentially landing on the next stone. If the frog’s last jump 
# was of size x, the frog’s next jump may be of size x - 1, x, or x + 1. 
# Given these following conditions return whether or not the frog can reach the other side.
# Note: The frog may only jump in the forward direction.

# Ex: Given the following stones…
# stones = [0, 1, 10], return false.
# This question is asked by Amazon. The frog can jump from stone 0 to stone 1, 
# but then the gap is too far to jump to the last stone (i.e. the stone at position 10)

# Ex: Given the following stones…
# stones = [0, 1, 2, 4], return true.
# The frog can jump from stone 0, to stone 1, to stone 2, to stone 4.


def canCross(stones):
     # Write your code here
     if not stones:
          return False
     if len(stones) == 1:
          return True
     dp = {}
     for i in range(len(stones)):
          dp[stones[i]] = set()
     dp[stones[0]].add(1)
     for i in range(1, len(stones)):
          for j in dp[stones[i - 1]]:
               if j + stones[i] in dp:
                    dp[j + stones[i]].add(j)
               if j - stones[i] in dp:
                    dp[j - stones[i]].add(j)
     return stones[-1] in dp and len(dp[stones[-1]]) > 0 