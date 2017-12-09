#Zork Version0.9
#Author Andrew DiBella
#Date: 24 November 2017


from classesZork import Player, Locale
import sys
from graphics import *


def mainGame():

    #Locations list
    longDescript = [
                "You are at Castle Black. The Night's Watch is preparing \nfor battle. It's extremly cold and tensions are high."
            ,   "You are at Winterfell. The Starks welcome you. Sansa Stark is the Queen and all of Winterfell is looking for your help." 
            ,   "You are at King's Landing. Good luck with Cersei Lannister. Home of the Iron Throne. " 
            ,   "You are in Dragonstone. Don't piss off the dragons. Khalessi, the Mother of Dragons, welcomes you." 
            ,   "You are on the Iron Islands. Watch out for sharks. Its windy and you don't really know where to go." 
            ,   "You are north of the Wall. Watch out for White Walkers. The Night King is coming for you. Defeat him to save Westeros"
            ,   "You are in Highgarden, home of House Tyrell. Careful not to be decieved by anyone." 
            ,   "You are at Braavos, the Free city. The real question is who really are you?"
            ,   "You are in a dark eerie Cave. Don't make too much noise. You can see something reflecting light in the distance."
            ,   "You are at The Arena, get ready for battle. Only a true warrior can make it out alive."
            ,   "You are at the Veil, one of the most scenic castles in Westeros. I think Little Finger may be up to something."
            ,   "You are docked on the Iron Vessel, the largest ship ever known to Westeros. Don't worry you won't get sea sick."
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
            ,   "You are at the Veil."
            ,   "You are on the Iron Vessel."

        ]

    items = ["Map", "Needle Sword", "Oathkeeper Sword", None, None, None, "Boat", "Dragon Glass Dagger", "Valyrian Steel Sword", None, None,None]

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
            ,   Locale("The Veil",longDescript[10], shortDescript[10], items[10])
            ,   Locale("The Iron Vessel",longDescript[11], shortDescript[11], items[11])
                 ]


                #north  #south  #east #west
    world =    [ [5,    1,      3,    None]  #CasBlack 0 
            ,    [0,    6,      2,    4   ]  #Winterfell 1
            ,    [3,    7,      None, 1   ]  #KingsLanding 2
            ,    [8,    2,      None, 0   ]  #Dragonstone 3
            ,    [11,   None,   1,    None]  #IronIslands 4
            ,    [None, 0,      None, None]  #NorthWall 5
            ,    [1,    None,   7,    9   ]  #HighGarden 6 
            ,    [2,    None,   10,   6   ]  #Braavos 7
            ,    [None, 3,      None, None]  #TheCave 8
            ,    [None, None,   6,    None]  #theArena 9
            ,    [None, None,   None, 7   ]  #theVeil 10
            ,    [None, 4,      None, None]  #ironVessel 11

        ]
    #Creates Player Object
    player = Player(setCharacter())
    player.setAttributes()
    player.setDifficulty()
    
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
                    "Search\n\n"
                    "Take (Item)\n"
                    "Drop (Item)\n"
                    "Equip (Item) \n\n"
                    "Menu\n"
                    "Inventory\n"
                    "Map\n"
                    )
            continue
            
        elif player.cmd == "quit":
            exit()

        elif player.cmd == "inventory":
            player.showInventory()
            continue

        elif player.cmd == "menu":
            player.displayMenu(locale)
            continue

        #Shows location Description 
        elif player.cmd[0:4] == "look":
            player.describe(locale)
            continue

        elif player.cmd == "search":
            player.search(locale)
            continue
        
        #Displays map
        if "Map" in player.inventory:
            guiMap()
                

        elif player.cmd[0:4] == "take":
            player.take(locale, items)
            continue

        elif player.cmd[0:4] == "drop":
            player.drop(locale)
            continue

        elif player.cmd[0:5] == "equip":
            player.equipItem()
            continue
            
        
        #Moves player
        elif player.cmd== "north" or player.cmd == "south" or player.cmd == "east" or player.cmd == "west":
            player.move(world,locale)

            
            
        #Winterfell Alliance
        if player.curLoc == 1:
            locale[player.curLoc].winterfell(player)

        #Hound
        if player.curLoc == 9:
            if locale[player.curLoc].hound == False:
                locale[player.curLoc].houndBattle(player)


        #North of Wall
        if player.curLoc == 5:
            locale[player.curLoc].finalBattle(player, locale)
            cmd = input("\n\nWould you like to play again?\n"
                        "Yes/No: ").lower()
            if cmd == "yes":
                titleIntro()
                mainGame()

            else:
                print("Thanks for playing!")
                sys.exit()

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

            

def guiMap():

    win = GraphWin("Map", 480, 360)
    win.setCoords(0,0,10,10)
    locs= [
    Text(Point(5,8.5),"North Wall" ).draw(win),
    Text(Point(5,6.5),"Castle Black").draw(win),
    Text(Point(5,4.5),"Winterfell").draw(win),
    Text(Point(5,2.5),"High Garden").draw(win),
    Text(Point(2 ,2.5),"The Arena").draw(win),
    Text(Point(2 ,4.5),"Iron Islands").draw(win),
    Text(Point(2 ,5.5),"Iron Vessel").draw(win),
    Text(Point(8, 2.5),"Braavos").draw(win),
    Text(Point(9.5,2.5),"Veil").draw(win),
    Text(Point(8,4.5),"Kings Landing").draw(win),
    Text(Point(8, 6.5), "Dragonstone").draw(win),
    Text(Point(8, 7.5), "The Cave").draw(win)
    ]

    locs[0].setTextColor("Red")

    lines= [
    Line(Point(5,8.3),Point(5,6.7)).draw(win),#NW to CB
    Line(Point(5,6.3), Point(5,4.7)).draw(win),#CB toWF
    Line(Point(5,4.3), Point(5,2.7)).draw(win),#WF to HG
    Line(Point(2,5.3), Point(2,4.7)).draw(win),#IV to II
    Line(Point(8, 7.3), Point(8,6.7)).draw(win),#C to DS
    Line(Point(8,6.3), Point(8,4.7)).draw(win),#DS to KL
    Line(Point(8,4.3), Point(8,2.7)).draw(win),#KL to B
    Line(Point(2.5,4.5),Point(4.5,4.5)).draw(win),#II to WF
    Line(Point(2.5,2.5),Point(4.3,2.5)).draw(win), #A to HG
    Line(Point(5.7,2.5),Point(7.5,2.5)).draw(win),#HG to B
    Line(Point(8.5,2.5),Point(9.3,2.5)).draw(win),#B to V
    Line(Point(5.6,4.5),Point(7.2,4.5)).draw(win),#WF to KL
    Line(Point(5.7,6.5),Point(7.3,6.5)).draw(win)#CB to DS
    
    
    ]

    
    
    
    

def main():
    #Stack
    titleIntro()
    mainGame()



main()

    
