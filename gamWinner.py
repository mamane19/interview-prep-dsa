# Two players are playing a game where white or black pieces are represented by a string, colors.
# The game rules are as follows:
# - Wendy  moves first and then they take alternate turns.
# - With each move Wendy may remove a white piece that has adjacent white pieces on both sides.
# - Likewise, with each move, Bob may remove a black piece that has adjacent black pieces on both sides.
# - After a piece is removed, the string is reduced in size by one piece. For instance, removing 'Y' from
# 'XYZ' results in 'XZ'.
# - When a player can no longer move, they have lost the game.

# Example:
# colors = 'wwwbbbbwww'
# Wendy  removes the piece 'w' at index 1, colors = 'wwbbbwww'.
# Bob removes the piece 'b' at index 3, colors = 'wwbbbwww'.
# Wendy removes the piece 'w' at index 6, colors = 'wwbbbww'.
# Bob removes the piece 'b' at index 3, colors = 'wwbbww'.
# Wendy has no more moves and is out of the game. Bob wins.

# Determine who wins if Wendy and Bob play with optimum skill.
# Return "Bob" if Bob wins and "Wendy" if Wendy wins.

# Function description:
# Complete the function gameWinner in the editor below. It must return a string, either "Bob" or "Wendy".
# GameWinner has the following parameter(s):
# String colors: each colors[i] represents the color located at index i within the colors string.
# returns : A string: the winner of the game either "Bob" or "Wendy".

# Sample Case 0:
# STDIN: wwwbb --> Function: colors = 'wwwbb'
# Sample Output 0:
# Wendy
# Explanation 0:
# There are five colors in the string. Wendy can remove any of the white pieces in the first move.
# After that, the colors string becomes 'wwbb'.  Bob has no move since there is no black piece with
# exactly two black adjacent pieces. So Wendy wins.


def gameWinner(colors):
    if "b" not in colors and len(colors) == 2:
        return "bob"
    wendy = 0
    bob = 0
    for i in range(len(colors)):
        if colors[i] == "w":
            wendy += 1
        elif colors[i] == "b":
            bob += 1
    if wendy > bob:
        return "wendy"
    elif wendy < bob:
        return "bob"
    else:
        return "bob"


# Typosquats are when an attacker registers a domain that appears similar to another, 
# with the intent to deceive visitors into believing they’re on the real website. For example, 
# palantir.cm is a typoSquatting of palantir.com. . You have been given a list of real company domains 
# to track, and a list of newly-registered domains. You have been asked to detect typosquats of the 
# real company domains in the newly-registered domains. Domains in both lists are of the form name.host,
# where name is a string representing the company name or website (with no internal periods),
# and host is the rest of the domain name (with any number of internal periods). 
# All domains are lowercase.

# Task 1
# The first kind of typosquat you have been asked to detect is URLs that use the same 
# name as a company, but have a different host. . You should not register an exact match as a 
# typosquat as companies may have recently registered or re-registered their domain. 
# Additionally, companies may have multiple domains using the same company name but
# different hosts, so these should not be detected as typosquats of each other.

# Write a function which takes the list of company domains and the list of newly-registered 
# domains as parameters, and returns a list of domains which are possible typosquats of the 
# company domains you are tracking.

# Custom Input Format:
# Number of company domains
# company domain 1
# company domain 2
# ...
# company domain n
# Number of new domains
# new domain 1
# new domain 2
# ...
# new domain n

# Example:
# Input:
# 2
# palantir.com
# apple.com
# 4
# palantir.biz
# apple.org
# apple.com
# appleorchard.net

# Output:
# palentir.biz
# apple.org

# Explanation:
# palantir.biz is a typosquat of palantir.com, and apple.org is a typosquat of apple.com. 
# apple.com is not a typosquat of apple.com because they are an exact match.

# def typosquats(companyDomains, newDomains):
	# companies = []
	# for domain in companyDomains:
	# 	companies.append(domain.split('.')[0])
	# 	companies.append(domain.split('.')[1])

	# typosquats = []
	# for domain in newDomains:
	# 	if domain.split('.')[0] in companies:
	# 		# Let's check they are not an exact match
	# 		if domain not in companyDomains:
	# 			typosquats.append(domain)
	# return typosquats
