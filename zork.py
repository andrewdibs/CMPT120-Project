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
    rollerCoaster = "You are at the roller coaster"
    score = 0
    location = ""

    location = entrance
    print(location)
    
    input("Move to next location")
    location = ferrisWheel
    score= score +5
    print("Score:" + str(score))
    print(location)
    
    input("Move to next location")
    location = bridge
    score = score +5
    print("Score:" + str(score))
    print(location)
    
    input("Move to next location")
    location = rollerCoaster
    score = score +5
    print("Score:" + str(score))
    print(location)
    
    input("Move to next location")
    location = entrance
    score = score +5
    print("Score:" + str(score))
    print(location)
main()
    
