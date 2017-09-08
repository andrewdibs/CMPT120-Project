#Zork First Steps
#Author Andrew DiBella
#Date: 9 September 2017

def main():
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
    
