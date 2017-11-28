#Zork Version0.9
#Author Andrew DiBella
#Date: 24 November 2017

import sys
from classesZork import Player, Locale


def mainGame():

    #Global Variables 

    battle= False

    #Locations list
    longDescript = [
                "You are at Castle Black. The Night's Watch is preparing \nfor battle."
            ,   "You are at Winterfell. The Starks welcome you." 
            ,   "You are at King's Landing. Good luck with Cersei Lannister" 
            ,   "You are in Dragonstone. Don't piss off the dragons." 
            ,   "You are on the Iron Islands. Watch out for sharks." 
            ,   "You are north of the Wall. Watch out for White Walkers."
            ,   "You are in Highgarden, home of House Tyrell." 
            ,   "You are at Braavos, the Free city."
            ,   "You are in a dark eerie Cave. Don't make too much noise."
            ,   "You are at The Arena, get ready for battle. "
                    ]

    shortDescript = [
                "You are at Castle Black."
            ,   "You are at Winterfell."
            ,   "You are at King's Landing."
            ,   "You are in Dragonstone."
            ,   "You are on the Iron Islands."
            ,   "You are north of the Wall."
            ,   "You are in Highgarden."
            ,   "You are in Braavos."
            ,   "You are in a Cave."
            ,   "You are at the Arena."

        ]

    items = [None, "Boat", None, None, "Map", None, None, "Dragon Glass Dagger", "Valyrian Steel Sword", None]

    locale= [   Locale("Castle Black",longDescript[0],shortDescript[0], items[0])
            ,   Locale("Winterfell",longDescript[1],shortDescript[1], items[1])
            ,   Locale("King's Landing",longDescript[2],shortDescript[2], items[2])
            ,   Locale("Dragonstone",longDescript[3],shortDescript[3], items[3])
            ,   Locale("Iron Islands",longDescript[4],shortDescript[4], items[4])
            ,   Locale("North Wall",longDescript[5],shortDescript[5], items[5])
            ,   Locale("Highgarden",longDescript[6],shortDescript[6], items[6])
            ,   Locale("Braavos",longDescript[7],shortDescript[7], items[7])
            ,   Locale("Cave",longDescript[8],shortDescript[8], items[8])
            ,   Locale("Arena",longDescript[9],shortDescript[9], items[9])
                 ]


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
    #Creates Player Object
    player = Player(setCharacter(), setDifficulty())

    
    while True:

        if locale[0].count == 0:
                print(player.name.upper(),"!!!WAKE UP! We have to get the hell out "
                      "of here. Where should we go?")
                locale[0].count += 1
                    
        player.cmd = input("Enter Command: ").lower()
            
        if player.cmd == "help":
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
            
        elif player.cmd == "quit":
            exit()

        elif player.cmd == "menu":
            player.displayMenu(locale)
            continue

        #Shows location Description 
        elif player.cmd[0:4] == "look":
            lookAround()
            continue

        elif player.cmd == "search":
            player.search(locale)
            continue
        
        #Displays map
        elif player.cmd == "map":
            if "Map" in player.inventory:
                showMap()
                continue
            else:
                print("\n You don't have a map.\n")
                continue

        elif player.cmd[0:4] == "take":
            player.take(locale, items)
            continue

        elif player.cmd[0:4] == "drop":
            player.drop(locale)
            continue
        
        #Moves player
        elif player.cmd== "north" or player.cmd == "south" or player.cmd == "east" or player.cmd == "west":
            player.move(world,locale)
            
        #Winterfell Alliance
        if player.curLoc == 1:
            while locale[1].count == 1:
                sansaQues= input("You are greeted by Sansa Stark..\n Sansa: "+player.name +
                                 ", will you help us win this war?\nYes or no: ").lower()

                if sansaQues == "yes":
                    print("\nWinterfell thanks you. We will win this together.")
                    player.score += 5
                    break
                elif sansaQues == "no":
                    print("\nJust remember who the real enemy is..")
                    break
            
 
        if player.curLoc == 9:
            if battle == False:
                while True:
                    response = input("The Hound challenges you to battle.\n"
                                      "Do you accept? Yes/No: ")
                    if response == "yes":
                        if "Valyrian Steel Sword" in player.inventory:
                            print("\n You used your sword to take down the hound.\n")
                            
                            player.inventory.append("Armor")
                            print("You took the Hounds armor.\n\n"
                                  "Armor has been added to your inventory.")
                            battle = True
                            break

                        else:
                            print("\nYou were killed by the Hound.")
                            conclusion()
                            sys.exit()
                    

                    elif response == "no":
                        print("Hound: AHAHA, come back when your ready to fight.")
                        break
                    
        #North of Wall
        if player.curLoc == 5:

            if "Armor" in player.inventory and "Valyrian Steel Sword" in player.inventory:
                winGame()
                break
                
            else:
                loseGame()
                break


        elif player.cmd != "north" and player.cmd != "south" and player.cmd != "east" and player.cmd!= "west": 
            print("Invalid command.")

        if locale[player.curLoc].count == 1:
            print("\n",locale[player.curLoc].beforeVisit, "\n")
        else:
            print("\n", locale[player.curLoc].afterVisit, "\n")

        player.moves -= 1

        if player.moves <0 :
            print("You used all of your moves.")
            loseGame()
            break
            
            

    
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
            print("Invalid command\n")


def loseGame():
    print("You were killed by White Walkers and Westeros has been overrun..")
    
        
def winGame():
    print("You took down the Night King and the undead Army!!!")
    
    
def conclusion():
    print(    "\n==\n"
              "Copyright (c) Andrew DiBella       Andrew.DiBella1@marist.edu")

def main():
    #Stack
    titleIntro()
    mainGame()
    conclusion()


main()

    
