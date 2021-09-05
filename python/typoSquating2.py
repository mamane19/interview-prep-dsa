# You are given a list of company domains and new domains. You are supposed to detect typosquats 
# of the company domains in new domains. domains are in list of form name.host where name represents 
# the company and host is the rest of the domain.

# Task 1:
# Detect domains that use the same name as the company but have a different host.

# Input:
# ['palantir.com','apple.com'],['palantir.biz','apple.org','apple.com','appleorchard.net']

# Output:
# ['palantir.biz', 'apple.org']

# Task 1 Solution:
# def typoSquating1(companyDomains, newDomains):
#     companies = []
#     for domain in companyDomains:
# 	    companies.append(domain.split('.')[0])
# 	    companies.append(domain.split('.')[1])

#     typosquats = []
#     for domain in newDomains:
# 	    if domain.split('.')[0] in companies:
# 			# Let's check they are not an exact match
# 		    if domain not in companyDomains:
# 			    typosquats.append(domain)
#     return typosquats

# Task 2:
# Detect those typosquats that replace characters in the domain with 
# any number of other similar looking characters.

# Task2 should also work for Task1.

# Characters that look similar:
# ['1', 'i', 'l', '!', '|']
# ['s', '5', '$']
# ['o', '0']
# ['a', '@']
# ['e', '3']

# Input:
# ['palantir.com','nic.ci'],['paiantir.com','nic.cl','palantirtechnologies.com','nlc.biz']

# Output:
# ['paiantir.com', 'nic.cl', 'nlc.biz']

# Task 2 Solution:
def typoSquating2(companyDomains, newDomains):
    """

    """



# if __name__ == '__main__':
#     companyDomains = ['palantir.com','nic.ci']
#     newDomains = ['paiantir.com','nic.cl','palantirtechnologies.com','nlc.biz']
#     print (typoSquating2(companyDomains, newDomains))







# Task 3:
# Detect those kind of typosquats that contains maximum of one adjacent swapped characters in the domain.

# Task3 should also work for Task2 and Task1.

# Input:
# ['palantir.com','apple.com'],['plaantir.com','aplantirtechnologies.com','palanti.rbiz']

# Output:
# ['plaantir.com', 'palanti.rbiz']

