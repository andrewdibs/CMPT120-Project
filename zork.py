#Zork Version0.5
#Author Andrew DiBella
#Date: 15 Oct 2017



def main():
    

    def mainGame():

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
                    
        score = 0
        curLocation = location[0]
        character = ""
    
    #Boolean Variables
        hasBeenThere = [     #### LIST KEY #####
                                
                        True    #CasBlack[0]
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

    #Start of Game
        titleIntro()
        character = setCharacter()
            
        while True:

            if countHasBeen[0] == 0:
                    print(character,"!!!WAKE UP! We have to get the hell out "
                          "of here. Where should we go?")
                    
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
            
            if command == "quit":
                exit()

            if command == "menu":
                print(showMenu(score, character, curLocation))
                continue

                
        #Castle Black
            if curLocation == location[0]:
                hasBeenThere[0] = True

                if countHasBeen[0] < 1:
                    score += 5

                countHasBeen[0] += 1
                
                if command == "north":
                    curLocation = location[5]
                elif command == "south":
                    curLocation = location[1]
                elif command == "east":
                    curLocation = location[3]
                else:
                    print("Invalid command.")

                    
        #North of Wall
            elif curLocation == location[5]:
                hasBeenThere[5] = True

                if countHasBeen[5] < 1:
                    score += 5

                countHasBeen[5] += 1

                if score < 25:
                    print("Why the hell would you go beyond the wall..")
                    break
                else:
                    print(character,", it's time to take down the Night King.")
                    break

        #Winterfell
            elif curLocation == location[1]:
                hasBeenThere[1] = True

                if countHasBeen[1] < 1:
                    score += 5

                countHasBeen[1] += 1

                if countHasBeen[1] == 1:
                    sansaQues= input("You are greeted by Sansa Stark..\n Sansa: "+character +
                                     ", will you help us win this war?\nYes or no: ").lower()
                    if sansaQues == "yes":
                        print("\nWinterfell thanks you. We will win this together.")
                        score += 5 
                    if sansaQues == "no":
                        print("\nJust remember who the real enemy is..")
                        
                if command == "west":
                    curLocation = location[4]
                elif command == "east":
                    curLocation = location[2]
                elif command == "north":
                    curLocation = location[0]
                else:
                    print("Invalid command.")

        #Kings Landing
            elif curLocation == location[2]:
                hasBeenThere[2] = True

                if countHasBeen[2] < 1:
                    score += 5

                countHasBeen[2] +=1

                if command == "north":
                    curLocation = location[3]
                elif command == "west":
                    curLocation = location[1]
                else:
                    print("Invalid command.")

                    
        #Dragonstone                   
            elif curLocation == location[3]:
                hasBeenThere[3] = True

                if countHasBeen[3] < 1:
                    score += 5

                countHasBeen[3] += 1
                
                if command == "south":
                    curLocation = location[2]
                elif command == "west":
                    curLocation = location[0]
                else:
                    print("Invalid command.")


         #Iron Islands                   
            elif curLocation == location[4]:
                hasBeenThere[4] = True

                if countHasBeen[4] == 1:
                    score += 5

                countHasBeen[4] += 1

                if command == "east":
                    curLocation = location[1]
                else:
                    print("Invalid command.")

            printLocation(curLocation)

    
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

    def showMenu(score, character ,curLocation):

        menu = ( "\n\n\t\t\tMain Menu\n"
                 "\t\t   ==================\n"+character+
                 "\nScore:" + str(score) +
                 "\nMoves Remaining: "+
                 "\nCurrent Location: "+ curLocation+"\n\n")
        return menu
        
          
    def printLocation(curLocation):
        print(curLocation, "\n")
        
        
    
    def conclusion():
        print("You were killed by White Walkers and Westeros has been overrun"
              "..\n==\n"
              "Copyright (c) Andrew DiBella       Andrew.DiBella1@marist.edu")


    #Stack
    mainGame()
    conclusion()


main()
    
