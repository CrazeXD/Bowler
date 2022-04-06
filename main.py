import function
import sys
file = open("bowlernames.txt", "w+")

print("Welcome to BowlOptimize!")
while True:
    print("Enter one of the following options: \n1. Reset Bowlers \n2. Add Bowlers \n3.Execute Algorithm")
    choice = int(input())
    if choice==1:
        file.truncate()
    elif choice==2:
        end = True
        while end:
            name = input("Please enter the name of the new bowler:\n")
            file.writelines(name)
            file.writelines("\n")
            passer = input("Do you have more names? Enter Y for yes or N for no.\n")
            if passer.lower() == "n":
                end = False
    elif choice==3:
        file.close()
        obj = function.Bowler(input("How many lanes do you have?\n"))
        print(obj.createLanes())
        sys.exit()