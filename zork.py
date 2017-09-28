#Zork Version0.3
#Author Andrew DiBella
#Date: 26 September 2017



def main():
    

    def mainGame():

    #Instance Variables          
        castleBlack = "You are at Castle Black. The Night's Watch is preparing \nfor battle."
        winterfell  = "You are at Winterfell. The Starks welcome you."
        kingsLanding= "You are at King's Landing. Good luck with Cersei Lannister"
        dragonstone = "You are in Dragonstone. Don't piss off the dragons."
        ironIslands = "You are on the Iron Islands. Watch out for sharks."
        northWall   = "You are north of the Wall. Watch out for White Walkers."
        score = 0
        location = castleBlack
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
            
            scoreLocation(location, score)
            
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
            if location == castleBlack:
                countCasBlack += 1
                visitCasBlack = True
                
                if command == "north":
                    location = northWall
                    score += 5
                elif command == "south":
                    location = winterfell
                    score += 5
                elif command == "east":
                    location = dragonstone
                else:
                    print("Invalid command.")

                    
        #North of Wall
            elif location == northWall:
                countNorthWall += 1
                visitNorthWall = True
                
                if score < 25:
                    print("Why the hell would you go beyond the wall..")
                    break
                else:
                    print(character, ", it's time to take down the Night King.")
                    break

        #Winterfell
            elif location == winterfell:
                countWinterfell += 1
                visitWinterfell = True
                
                if command == "west":
                    location = ironIslands
                    score += 5
                elif command == "east":
                    location = kingsLanding
                    score += 5
                elif command == "north":
                    location = castleBlack
                    score += 5
                else:
                    print("Invalid command.")

        #Kings Landing
            elif location == kingsLanding:
                countKingsLanding +=1
                visitKingsLanding = True

                if command == "north":
                    location = dragonstone
                elif command == "west":
                    location = winterfell
                else:
                    print("Invalid command.")

                    
        #Dragonstone                   
            elif location == dragonstone:
                countDragonstone += 1
                visitDragonstone = True
                
                if command == "south":
                    location = kingsLanding
                elif command == "west":
                    location = castleBlack
                else:
                    print("Invalid command.")


         #Iron Islands                   
            elif location == ironIslands:
                countIronIslands += 1
                visitIronIslands = True

                if command == "east":
                    location = winterfell
                else:
                    print("Invalid command.")
    
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


          
    def scoreLocation(location, score):
        print(location)
        print("Score: ", score, "\n")
        
    
    def conclusion():
        print("You were killed by White Walkers and Westeros has been overrun"
              "..\n==\n"
              "Copyright (c) Andrew DiBella       Andrew.DiBella1@marist.edu")


    #Stack
    mainGame()
    conclusion()


main()
    
