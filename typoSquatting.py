  
	
# Task 2
# The second kind of typosquat you have been asked to detect is those that replace characters 
# in the domain with other similar-looking characters. For example, attackers may replace 
# l (lowercase L) with |  (pipe character), or o  (lowercase O) with 0  (zero), because they may 
# appear similar in common fonts and can go undetected. Attackers may replace any number of characters 
# in the domain with similar-looking characters. A complete list of common character replacements is 
# provided below.

# Consufable characters:
# 1 i l ! |
# s 5 $
# o 0
# a @
# e 3

# Write a function which takes the list of company domains and the list of newly-registered domains 
# as parameters, and returns a list of domains which are possible typosquats of the company domains 
# you are tracking.

# E.g.
# Input:
# ['palentir.com', 'nic.ci']
# ['palentir.com', 'nic.cl', 'palentirtechnologies.com', 'ncl.biz']
# Output:
# ['paiantir.com', 'nic.cl', 'nlc.biz']

def find_typosquats(company_domains, new_domains):
    possible_typosquats = []


# if __name__ == '__main__':
#     company_domains = ['palentir.com', 'nic.ci']
#     new_domains = ['palentir.com', 'nic.cl', 'palentirtechnologies.com', 'ncl.biz']
#     print (find_typosquats(company_domains, new_domains))





# if __name__ == '__main__':
#     companyDomains = ['palantir.com','nic.ci']
#     newDomains = ['paiantir.com','nic.cl','palantirtechnologies.com','nlc.biz']
#     print (typosquats2(companyDomains, newDomains))


