#Zork Version0.7
#Author Andrew DiBella
#Date: 15 Oct 2017

score = 0
curLocation = ""
hasBeenThere = []
locDescript = []
countHasBeen = []
searched = []
items = []
locale = []
world = []
locIndex = 0
def mainGame():

    #Global Variables 
    global score
    global curLocation
    global hasBeenThere 
    global locDescript 
    global countHasBeen
    global searched
    global locale
    global world
    global locIndex
    global items

    #Locations list
    locDescript = [
                "You are at Castle Black. The Night's Watch is preparing \nfor battle."
            ,   "You are at Winterfell. The Starks welcome you." 
            ,   "You are at King's Landing. Good luck with Cersei Lannister" 
            ,   "You are in Dragonstone. Don't piss off the dragons." 
            ,   "You are on the Iron Islands. Watch out for sharks." 
            ,   "You are north of the Wall. Watch out for White Walkers."
            ,   "You are in Highgarden, home of House Tyrell." 
            ,   "You are at Braavos, the Free city."
            ,   "You are in a dark eerie Cave."
            ,   "You are at The Arena, get ready for battle. "
                    ]

    locale = ["Castle Black", "Winterfell", "Kings Landing", "Dragonstone",
                "Iron Islands", "North of Wall", "High Garden", "Braavos",
                "The Cave", "The Arena" ]

    searched = [False, False, False, False, False, False, False, False, False, False]

    items = [None, None, None, None, "Map", None, None, None, "Valyrian Steel Sword", "Armor"]
    
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
                ,   False   #TheCave[8]
                ,   False   #theArena[9]
                    ]

    #Number of times each location has been visited
    countHasBeen = [0,0,0,0,0,0,0,0,0,0]

                #north  #south  #east #west
    world =    [ [5,    1,      3,    None]  #CasBlack 0 
            ,    [0,    6,      2,    4   ]  #Winterfell 1
            ,    [3,    7,      None, 1   ]  #KingsLanding 2
            ,    [8,    2,      None, 0   ]  #Dragonstone 3
            ,    [None, None,   1,    None]  #IronIslands 4
            ,    [None, 0,      None, None]  #NorthWall 5
            ,    [1,    None,   7,    9   ]  #HighGarden 6 
            ,    [2,    None,   None, 6   ]  #Braavos 7
            ,    [None, 3,      None, None]  #TheCave 8
            ,    [None, None,   6,    None]  #theArena 9

        ]
    
    moves = setDifficulty()
    curLocation = locale[0]
    character = ""

    character = setCharacter()          
    while True:

        if countHasBeen[0] == 0:
                print(character,"!!!WAKE UP! We have to get the hell out "
                      "of here. Where should we go?")
                countHasBeen[0] += 1
                    
        cmd = input("Enter Command: ").lower()
            
        if cmd == "help":
            print("Possible commands:\n"
                    "Help\n"
                    "Quit\n\n"
                    "North\n"
                    "South\n"
                    "East\n"
                    "West\n\n"
                    "Look Around\n"
                    "Search\n"
                    "Take\n\n"
                    "Menu\n"
                    "Map\n"
                    )
            continue
            
        elif cmd == "quit":
            exit()

        elif cmd == "menu":
            print(showMenu(score, character, moves, curLocation))
            continue

        #Shows location Description 
        elif cmd[0:4] == "look":
            lookAround()
            continue

        elif cmd == "search":
            searchArea()
            continue
        
        #Displays map
        elif cmd == "map":
            showMap()
            continue

        #Moves player
        elif cmd== "north" or cmd == "south" or cmd == "east" or cmd == "west":
            whereTo(locIndex, cmd)

        #Winterfell Alliance
        if curLocation == locale[1]:
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
            
 

                    
        #North of Wall
        if curLocation == locale[5]:

            if score < 25:
                print("Why the hell would you go beyond the wall..")
                break
            else:
                print(character,", it's time to take down the Night King.")
                break

        elif cmd != "north" and cmd != "south" and cmd != "east" and cmd!= "west": 
            print("Invalid command.")

        printLocation(curLocation)
        moves -= 1

        if moves <0 :
            conclusion()
            quit()

    
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
              "<                            *            The Cave         >\n"
              "<                            *               *             >\n"
              "<                      Castle Black-----DragonStone        >\n"
              "<                            *               *             >\n"
              "<                            *               *             >\n"
              "<                            *               *             >\n"
              "<      IronIslands------Winterfell------KingsLanding       >\n"
              "<                            *               *             >\n"
              "<                            *               *             >\n"
              "<                            *               *             >\n"
              "<        The Arena------HighGarden--------Braavos          >\n"
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
    global locale
    
    curLocation = locale[i]
  
    if not hasBeenThere[i]:
        score += 5

    hasBeenThere[i] = True
    countHasBeen[i] += 1

def whereTo(curLocation, direct):
    global world
    global locIndex

    numDirect= None
    if direct == "north":
        numDirect = 0
    elif direct == "south":
        numDirect = 1
    elif direct == "east":
        numDirect = 2
    elif direct == "west":
        numDirect = 3

    newLoc = world[curLocation][numDirect]
    

    if newLoc is None:
        print("Wrong Way.")

    else:
        locIndex= newLoc
        goTo(newLoc)
        

       

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

def lookAround():
    print(locDescript[locIndex])
        
def searchArea():
    global items
    global searched
    global locIndex
    print("DEBUG:",locIndex)
    if items[locIndex] != None:
        print("Look there's a", items[locIndex])
        searched[locIndex] = True

    else:
        print("There is nothing here.")

    
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

    
