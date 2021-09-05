# write a function that takes a time in the string format of "HH:MM" and returns
# a multiline string where the hours are drawn on the left and the minutes are
# drawn on the right. The output should look like this:
##### #####       ##### #####
#   # #   #   #   #   # #   #
##### #####       ##### #####
#   # #   #   #   #   # #   #
##### #####       ##### #####
# the #'s should be filled in with the numbers 0-9
# you can use an OOP approach to this problem, but it should be done without
# using any string methods.


class DigitalClock(object):
    def __init__(self):
        self.clock = "HH:MM"

    def __str__(self):
        return self.clock

    def setClock(self, clock):
        self.clock = clock

    def getClock(self):
        return self.clock

    numbers = {
        "1": ["#", "#", "#", "#", "#"],
        "2": ["#####", "    #", "#####", "# ", "#####"],
        "3": ["#####", "    #", "#####", "    #", "#####"],
        "4": ["#   #", "#   #", "#####", "    #", "    #"],
        "5": ["#####", "# ", "#####", "    #", "#####"],
        "6": ["#####", "# ", "#####", "#   #", "#####"],
        "7": ["#####", "    #", "    #", "    #", "    #"],
        "8": ["#####", "#   #", "#####", "#   #", "#####"],
        "9": ["#####", "#   #", "#####", "    #", "#####"],
        "0": ["#####", "#   #", "#   #", "#   #", "#####"],
        ":": ["     ", "  #  ", "     ", "  #  ", "     "],
    }

    def makeClock(self, clockList):
        clockList = [char for char in self.clock]
        for i in range(len(self.numbers["1"])):
            for j in range(len(clockList)):
                print(self.numbers[clockList[j]][i] + "\t", end="")
            print()


if __name__ == "__main__":
    clock = DigitalClock()
    clock.setClock("12:30")
    clock.makeClock(clock.getClock())
