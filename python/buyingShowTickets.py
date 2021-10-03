# Alex plans on visiting the museum and is at the counter to purchase passes for the same. 
# The administrators have decided not to sell group passes, and are providing only one pass at a time. 
# If a visitor needs more than one pass, he/she has to pass through the queue again to reach the counter 
# and buy the next pass. Alex wants to buy many passes.

# Considering that the visitors and number of passes each visitor needs is known, how much time does Alex require 
# to buy all passes? Alex's place in the queue to the counter will be given, and each transaction takes 1 unit of time. 
# The time needed to go to the back of the line each time can be ignored.

def waitingTime(tickets, p):
    return sum([min(tickets[i], tickets[p]) if i<=p else min(tickets[i], tickets[p] - 1) for i in range(len(tickets))])


# print(waitingTime([2,6,3,4,5],2))
# print(waitingTime2([2,6,3,4,5],2))

if __name__ == "__main__":
    print(waitingTime([2,6,3,4,5], 2))



