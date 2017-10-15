#Zork Version0.5
#Author Andrew DiBella
#Date: 15 Oct 2017



def main():
    

    def mainGame():

    #Locations list
        location = [
                    "You are at Castle Black. The Night's Watch is preparing \nfor battle.",
                    "You are at Winterfell. The Starks welcome you." , 
                    "You are at King's Landing. Good luck with Cersei Lannister" ,
                    "You are in Dragonstone. Don't piss off the dragons." ,
                    "You are on the Iron Islands. Watch out for sharks." ,
                    "You are north of the Wall. Watch out for White Walkers.",
                    "You are in Highgarden, home of House Tyrell." ,
                    "You are at Braavos, the Free city."
                    ]
                    
        score = 0
        curLocation = location[0]
        character = ""
    
    #Boolean Variables
        visitCasBlack = True
        visitWinterfell = False
        visitKingsLanding = False
        visitDragonstone = False
        visitIronIslands = False
        visitNorthWall = False

    #Number of times each location has been visited
        countCasBlack = 0
        countWinterfell = 0
        countKingsLanding = 0
        countDragonstone = 0
        countIronIslands = 0
        countNorthWall = 0

    #Start of Game
        titleIntro()
        character = setCharacter()

    #Starting character chosen print statement
        if character == "Jon Snow":
            print("You are Jon Snow, King of the North.")
        if character == "Jaime":
            print("You are Jaime Lannister, deadly even with one hand.\n")
        if character == "Arya":
            print("You are Arya Stark, I worry for anyone who gets in your way.\n")
        if character == "Tyrion":
            print("You are the dwarf Tyrion Lannister, you drink and know things\n")
            
        

        while True:
            
            
            if countCasBlack == 0:
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
                      "Quit\n")
            if command == "quit":
                exit()

                
        #Castle Black
            if curLocation == location[0]:
                visitCasBlack = True

                if countCasBlack < 1:
                    score += 5

                countCasBlack += 1
                
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
                visitNorthWall = True

                if countNorthWall < 1:
                    score += 5

                countNorthWall += 1

                if score < 25:
                    print("Why the hell would you go beyond the wall..")
                    break
                else:
                    print(character,", it's time to take down the Night King.")
                    break

        #Winterfell
            elif curLocation == location[1]:
                visitWinterfell = True

                if countWinterfell < 1:
                    score += 5

                countWinterfell += 1

                if countWinterfell == 1:
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
                visitKingsLanding = True

                if countKingsLanding < 1:
                    score += 5

                countKingsLanding +=1

                if command == "north":
                    curLocation = location[3]
                elif command == "west":
                    curLocation = location[1]
                else:
                    print("Invalid command.")

                    
        #Dragonstone                   
            elif curLocation == location[3]:
                visitDragonstone = True

                if countDragonstone < 1:
                    score += 5

                countDragonstone += 1
                
                if command == "south":
                    curLocation = location[2]
                elif command == "west":
                    curLocation = location[0]
                else:
                    print("Invalid command.")


         #Iron Islands                   
            elif curLocation == location[4]:
                visitIronIslands = True

                if countIronIslands == 1:
                    score += 5

                countIronIslands += 1

                if command == "east":
                    curLocation = location[1]
                else:
                    print("Invalid command.")

            scoreLocation(curLocation, score)

    
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
                break
            
            if character[0:3] == "ary":
                character = "Arya"
                break
            
            if character[0:3] == "tyr":
                character = "Tyrion"
                break
            
            if character[0:3] == "jai":
                character = "Jaime"
                break
            
            else:
                print("Not valid character name.")

        return character


          
    def scoreLocation(curLocation, score):
        print(curLocation)
        print("Score: ", score, "\n")
        
    
    def conclusion():
        print("You were killed by White Walkers and Westeros has been overrun"
              "..\n==\n"
              "Copyright (c) Andrew DiBella       Andrew.DiBella1@marist.edu")


    #Stack
    mainGame()
    conclusion()


main()
    
