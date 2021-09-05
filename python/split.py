# separate a string into two equal parts
# for example, NOKNOK returns (NOK, NOK)

def split(string):
    string = string.strip()
    print(string[:len(string)//2], string[len(string)//2:])
split("NOKNOK")