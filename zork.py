#Zork First Steps
#Author Andrew DiBella
#Date: 9 September 2017

def main():

    #Title
    print("\t\t\tRunaway Train\n"
          "\t\t\t=============\n")
    #Back Story
    print("You are a roller coaster enthusiast and you finally found the opportunity\n"
          "to go to Six flags to ride the record breaking King da Ka.\n"
          "After a 3 hour long car ride you can finally see the monstrous ride and\n"
          "feel a little worried and you think to yourself\n\n"
          "Maybe the runaway train is a better option...\n")

    #Instance Variables          
    entrance= "You are at the Entrance of an amusement park"
    ferrisWheel= "You are at the Ferris Wheel"
    bridge = "You are sitting on the bridge"
    kingDaKa = "You are at King da Ka"
    score = 0
    location = ""

    #Starting Location 
    location = entrance
    print(location+"\n")

    #Ferriswheel
    input("Press Enter: Move to next location\n==\n")
    location = ferrisWheel
    score= score +5
    print("Score:" + str(score))
    print(location+"\n")

    #Bridge
    input("Press Enter: Move to next location\n==\n")
    location = bridge
    score = score +5
    print("Score:" + str(score))
    print(location+"\n")

    #RollerCoaster
    input("Press Enter: Move to next location\n==\n")
    location = kingDaKa
    score = score +5
    print("Score:" + str(score))
    print(location+"\n")

    #Entrance 2nd time
    input("Press Enter: Move to next location\n==\n")
    location = entrance
    score = score +5
    print("Score:" + str(score))
    print(location+"\n")

    #conclusion
    print("You decide that King da Ka wasn't a good idea and leave Six Flags with\n"
          "dissapointment..\n==\n"
          "Copyright (c) Andrew DiBella       Andrew.DiBella1@marist.edu")
main()
    
