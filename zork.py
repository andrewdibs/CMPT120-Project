#Zork First Steps
#Author Andrew DiBella
#Date: 9 September 2017

def main():

    #Title
    print("\t\t\t Game of Thrones\n"
          "\t\t\t=================\n")
    #Back Story
    print("Winter is coming....You've seen the first white walker beyond\n"
          "the wall and wake up from a short coma in Castle Black. You \n"
          "must warn the people to prepare for an attack.\n"
          "Who will you tell first? Who's side will you take?...\n"
          "\t======================================================\n")

    #Instance Variables          
    castleBlack = "You are at Castle Black. The Night's Watch is preparing for battle."
    winterfell  = "You are at Winterfell. The Starks welcome you."
    casterlyRock= "You are at Casterly Rock. Good luck with Cersei Lannister"
    dragonstone = "You are in Dragonstone. Don't piss off the dragons."
    ironIslands = "You are on the Iron Islands. Watch out for sharks."
    northWall   = "You are north of the Wall. Watch out for White Walkers."
    score = 0
    location = ""

    #Castle Black
    location = castleBlack
    print(location+"\n")

    #Winterfell 
    input("Press Enter: Move to next location\n==\n")
    location = winterfell
    score= score +5
    print("Score:" + str(score))
    print(location+"\n")

    #Casterly Rock 
    input("Press Enter: Move to next location\n==\n")
    location = casterlyRock
    score = score +5
    print("Score:" + str(score))
    print(location+"\n")

    #Dragonstone
    input("Press Enter: Move to next location\n==\n")
    location = dragonstone
    score = score +5
    print("Score:" + str(score))
    print(location+"\n")

    #North of the Wall 
    input("Press Enter: Move to next location\n==\n")
    location = northWall
    score = score +5
    print("Score:" + str(score))
    print(location+"\n")

    #conclusion
    print("You were killed by white walkers and westeros has been overrun"
          "..\n==\n"
          "Copyright (c) Andrew DiBella       Andrew.DiBella1@marist.edu")
main()
    
