# letters = {'a':" ***\n*   *\n*   *\n*****\n*   *\n*   *\n*   *",
#             'b': "****\n*   *\n*   *\n*   *\n*****\n*   *\n*   *\n*   *",
#             'c': " ***\n*   *\n*   *\n*   *\n*   *\n*   *\n*****",
#             'd': "***  \n*   *\n*   *\n*   *\n*   *\n*   *\n*   *",
#             'e': " ***\n*   *\n*****\n*   *\n*   *\n*   *\n ***",
#             'f': "***  \n*   *\n*   *\n*   *\n*   *\n*   *\n*   *",
#             }
# print(letters['f'])

numbers = {
    "1": " #\n #\n #\n #\n #",
    "2": " #####\n     #\n #####\n #\n #####",
    "3": " #####\n     #\n #####\n     #\n #####",
    "4": " #   #\n #   #\n #####\n     #\n     #",
    "5": " #####\n #\n #####\n     #\n #####",
    "6": " #####\n #\n #####\n #   #\n #####",
    "7": " #####\n     #\n     #\n     #\n     #",
    "8": " #####\n #   #\n #####\n #   #\n #####",
    "9": " #####\n #   #\n #####\n     #\n #####",
    "0": " #####\n #   #\n #   #\n #   #\n #####",
    ":": " \n #\n\n #\n"
}


dict_of_lists = {
    "1": [ ' # ',' # ',' # ',' # ',' # '],
    "2": [ ' #####','     #',' #####',' # ',' #####'],
    "3": [ ' #####','     #',' #####','     #',' #####'],
    "4": [ ' #   #',' #   #',' #####','     #','     #'],
    "5": [ ' #####',' # ',' #####','     #',' #####'],
    "6": [ ' #####',' # ',' #####',' #   #',' #####'],
    "7": [ ' #####','     #','     #','     #','     #'],
    "8": [ ' #####',' #   #',' #####',' #   #',' #####'],
    "9": [ ' #####',' #   #',' #####','     #',' #####'],
    "0": [ ' #####',' #   #',' #   #',' #   #',' #####'],
    ":": [ '   # ','   # ']
}
sep =  " \n #\n\n #\n"
def print_digit(newList):
    for i in range(len(dict_of_lists['1'])):
        for j in range(len(newList)):
            print(dict_of_lists[newList[j]][i], end='')
        print()

if __name__ == '__main__':
    print_digit(['1','4'])


# the middle.
    # def makeClock(self)r
    #     # let's make a blank string to hold the clock
    #     clockString = ""
    #     # let's use a for loop to go through the clock and turn it into a string
    #     for number in self.clock:
    #         # if the number is in the dictionary, then we'll add the 
    #         # number and the colon to the clock string
    #         if number in self.numbers:
    #             clockString += self.numbers[number] + "\n"
    #         # if the number is not in the dictionary, then we'll add a blank space
    #         else:
    #             clockString += " "
    #     # let's return the clock string on the same line
    #     return clockString.rstrip()
    for i in range(len(self.numbers["1"])):
            for j in range(len(clockList)):
                print(self.numbers[clockList[j]][i] + "", end="")
            print(":")



            
def makeClock(self, clockList):
        clockList = [char for char in self.clock]
        # Let's loop through the numbers and for each element we look throught the clock list
        # and get the 5 by 5 grid of the number and replace the number with the grid
                for number in clockList:
            for grid in self.numbers[number]:
                print(grid, end="")
            print("")


def makeClock(self, clockList):
        clockList = [char for char in self.clock]
        # Let's loop through the numbers and for each element we look throught the clock list
        # and get the 5 by 5 grid of the number and replace the number with the grid
                for num in clockList:
            for key in self.numbers:
                if num == key:
                    for i in range(5):
                        clockList[clockList.index(num)+i] = self.numbers[key][i]
        return clockList

