#imports
import sys

#Make the main class

class Bowler:
    #Initialize
    def __init__(self, lanecount):
        try:
            self.lanecount = int(lanecount)
        except:
            print("Error, lanecount must be an integer")
            sys.exit()
        if self.lanecount<1:
            print("Must have at least 1 lane")
            sys.exit()
                    
        bowlerfile = open("bowlernames.txt", "r")
        self.bowlers = []
        self.bowlercount = 0
        self.lanes = []
        for i in bowlerfile.readlines():
            if i.endswith("\n"):
                string = i.rsplit("\n")
                string = string[0]
            else:
                string = i
            self.bowlers.append(string)
            self.bowlercount += 1
        
    def createLanes(self):
        #Add the first lane
        self.lanes.append(self.bowlers)
        #check if its odd or even
        for i in range(1, self.lanecount):
            currentlane = []
            if self.bowlercount%self.lanecount == 0:
                offset = self.bowlercount/self.lanecount
                offset = int(offset)
                currentlane = self.bowlers[offset::] + self.bowlers[:offset:]
                self.bowlers = currentlane
            self.lanes.append(currentlane)
        return self.lanes

obj = Bowler(input("How many lanes do you have?\n"))

print(obj.createLanes())