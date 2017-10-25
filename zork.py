#Zork Version0.5
#Author Andrew DiBella
#Date: 15 Oct 2017

score = 0
curLocation = ""
hasBeenThere = []
location = []
countHasBeen = []

def mainGame():

    #Global Variables 
    global score
    global curLocation
    global hasBeenThere 
    global location 
    global countHasBeen 

    #Locations list
    location = [
                "You are at Castle Black. The Night's Watch is preparing \nfor battle."
            ,   "You are at Winterfell. The Starks welcome you." 
            ,   "You are at King's Landing. Good luck with Cersei Lannister" 
            ,   "You are in Dragonstone. Don't piss off the dragons." 
            ,   "You are on the Iron Islands. Watch out for sharks." 
            ,   "You are north of the Wall. Watch out for White Walkers."
            ,   "You are in Highgarden, home of House Tyrell." 
            ,   "You are at Braavos, the Free city."
                    ]

 
    moves = setDifficulty()
    curLocation = location[0]
    character = ""

    stats = [score,curLocation, moves, location ]
    
    #Boolean Variables
    hasBeenThere = [     #### LIST KEY #####
                                
                    False    #CasBlack[0]
                ,   False   #Winterfell[1]
                ,   False   #KingsLanding[2]
                ,   False   #Dragonstone[3]
                ,   False   #IronIslands[4]
                ,   False   #NorthWall[5]
                ,   False   #HighGarden[6]
                ,   False   #Braavos[7]
                    ]

    #Number of times each location has been visited
    countHasBeen = [0,0,0,0,0,0,0,0]
    
    character = setCharacter()          
    while True:

        if countHasBeen[0] == 0:
                print(character,"!!!WAKE UP! We have to get the hell out "
                      "of here. Where should we go?")
                countHasBeen[0] += 1
                    
        command = input("Enter Command: ").lower()
            
        if command == "help":
            print("Possible commands:\n"
                    "Help\n"
                    "North\n"
                    "South\n"
                    "East\n"
                    "West\n"
                    "Menu\n"
                    "Map\n"
                    "Quit\n")
            continue
            
        elif command == "quit":
            exit()

        elif command == "menu":
            print(showMenu(score, character, moves, curLocation))
            continue

        elif command == "map":
            showMap()
            continue

        #NORTH
        elif command == "north":

            if curLocation == location[0]:
                goTo(5)

            elif curLocation== location[1]:
                goTo(0)

            elif curLocation == location[6]:
                goTo(1)

            elif curLocation == location[7]:
                goTo(2)

            elif curLocation == location[2]:
                goTo(3)

            elif curLocation == location[7]:
                goTo(2)

            else:
                print("Wrong Way.")

        #SOUTH
        elif command == "south":

            if curLocation == location[0]:
                goTo(1)
                
                while countHasBeen[1] == 1:
                    sansaQues= input("You are greeted by Sansa Stark..\n Sansa: "+character +
                                     ", will you help us win this war?\nYes or no: ").lower()

                    if sansaQues == "yes":
                        print("\nWinterfell thanks you. We will win this together.")
                        score += 5
                        break
                    elif sansaQues == "no":
                        print("\nJust remember who the real enemy is..")
                        break
                
            elif curLocation == location[3]:
                goTo(2)

            elif curLocation == location[2]:
                goTo(7)

            elif curLocation == location[1]:
                goTo(6)

            else:
                print("Wrong Way.")
                

        #EAST
        elif command == "east":
            if curLocation == location[0]:
                goTo(3)

            elif curLocation == location[1]:
                goTo(2)

            elif curLocation == location[6]:
                goTo(7)

            elif curLocation == location[4]:
                goTo(1)

            else:
                print("Wrong Way.")

        #WEST
        elif command == "west":

            if curLocation == location[3]:
                goTo(0)

            elif curLocation == location[2]:
                goTo(1)

            elif curLocation == location[7]:
                goTo(6)

            elif curLocation == location[1]:
                goTo(4)


                    
        #North of Wall
        if curLocation == location[5]:

            if score < 25:
                print("Why the hell would you go beyond the wall..")
                break
            else:
                print(character,", it's time to take down the Night King.")
                break

        elif command != "north" and command != "south" and command != "east" and command!= "west": 
            print("Invalid command.")

        printLocation(curLocation)
        moves -= 1

    
def titleIntro():
        #Title
    print("\t\t\t Game of Thrones\n"
          "\t\t\t=================\n")
        #Back Story
    print("Winter is coming....You've seen the first white walker beyond\n"
              "the wall and wake up from a short coma in Castle Black. You \n"
              "must warn the people of Westeros to prepare for an attack.\n"
              "Who will you tell first? Who's side will you take?...\n"
              "\t======================================================\n")

def setCharacter():
        
    while True:
        userInput = input("Please choose a character:\n"
                              "Jon Snow\tTyrion Lannister\n"
                              "Arya Stark\tJaime Lannister\n"
                              "Enter character: \n")
        character = userInput.lower()
        
        if character[0:3] == "jon":
            character = "Jon Snow"
            print("You are Jon Snow, King of the North.\n")
            break
            
        if character[0:3] == "ary":
            character = "Arya"
            print("You are Arya Stark, I worry for anyone who gets in your way.\n")
            break
            
        if character[0:3] == "tyr":
            character = "Tyrion"
            print("You are the dwarf Tyrion Lannister, you drink and know things\n")
            break
            
        if character[0:3] == "jai":
            character = "Jaime"
            print("You are Jaime Lannister, deadly even with one hand.\n")
            break
            
        else:
            print("Not valid character name.")

    return character

def showMenu(score, character ,moves, curLocation):

    menu = ( "\n\n\t\t\tMain Menu\n"
                 "\t\t   ==================\n"+character+
                 "\nScore:" + str(score) +
                 "\nMoves Remaining: "+ str(moves) +
                 "\nCurrent Location: "+ curLocation+"\n\n")
    return menu

def showMap():
    print(  " ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
              "<                                                          >\n"
              "<                       North Wall                         >\n"
              "<                            *                             >\n"
              "<                            *                             >\n"
              "<                            *                             >\n"
              "<                      Castle Black-----DragonStone        >\n"
              "<                            *               *             >\n"
              "<                            *               *             >\n"
              "<                            *               *             >\n"
              "<      IronIslands------Winterfell------KingsLanding       >\n"
              "<                            *               *             >\n"
              "<                            *               *             >\n"
              "<                            *               *             >\n"
              "<                       HighGarden--------Braavos          >\n"
              "<                                                          >\n"
              "<                                                          >\n"
              " vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n")
              
          
def printLocation(curLocation):
    print(curLocation, "\n")

def goTo(i):
    global curLocation
    global score
    global hasBeenThere
    global countHasBeen
    
    curLocation = location[i]
  
    if not hasBeenThere[i]:
        score += 5

    hasBeenThere[i] = True
    countHasBeen[i] += 1
    

       

def setDifficulty():
    while True:
        cmd = input("Please Select Difficulty:\n"
                    "Easy\n"
                    "Medium\n"
                    "Hard\n"
                    "Realistic\n"
                    ">>:").lower()
        if cmd == "easy":
            return 100
        elif cmd[0:3] == "med":
            return 75
        elif cmd == "hard":
            return 50
        elif cmd[0:4] == "real":
            return 25
        else:
            print("Invalid command")
        
    
def conclusion():
    print("You were killed by White Walkers and Westeros has been overrun"
              "..\n==\n"
              "Copyright (c) Andrew DiBella       Andrew.DiBella1@marist.edu")

def main():
    #Stack
    titleIntro()
    mainGame()
    conclusion()


main()

    
