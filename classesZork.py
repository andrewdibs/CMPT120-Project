#classesZork.py
#Author Andrew DiBella
#Date 24 November 2017

import sys
from random import randint
class Player:


    def __init__(self, name):
        
        self.name = name
        self.inventory = [None,None,None,None,None,None,None,None,None,None,None,None]
        self.curLoc = 0
        self.cmd = ""
        self.score = 0
        self.curItem = ""
        self.strength = 0
        self.health = 0
        self.charisma = 0
        self.swiftness = 0

    def setDifficulty(self):
        while True:
            cmd = input("Please Select Difficulty:\n"
                        "Easy\n"
                        "Medium\n"
                        "Hard\n"
                        "Realistic\n"
                        ">>:").lower()
            if cmd == "easy":
                self.moves = 100
                self.numDifficulty= randint(0,50)
                break
            elif cmd[0:3] == "med":
                self.moves = 75
                self.numDifficulty= randint(50,100)
                break
            elif cmd == "hard":
                self.moves = 50
                self.numDifficulty= randint(100,150)
                break
            elif cmd[0:4] == "real":
                self.moves = 25
                self.numDifficulty= randint(150,200)
                break
            else:
                print("Invalid command\n") 

        
    def setAttributes(self):
        if self.name == "Jon Snow":
            self.strength = 95
            self.swiftness = 55
            self.charisma = 20
            self.health = 50
            self.curLoc = 0

        elif self.name == "Arya":
            self.strength = 40
            self.swiftness = 95
            self.charisma = 55
            self.health = 50
            self.curLoc = 1

        elif self.name == "Tyrion":
            self.strength = 35
            self.swiftness = 60
            self.charisma = 95
            self.health = 50
            self.curLoc = 3

        elif self.name == "Jaime":
            self.strength = 60
            self.swiftness = 50
            self.charisma = 65
            self.health = 50
            self.curLoc = 2
        
        
        
    def move(self, world, locale):
        
        numDirect= None
        if self.cmd == "north":
            numDirect = 0
        elif self.cmd == "south":
            numDirect = 1
        elif self.cmd == "east":
            numDirect = 2
        elif self.cmd == "west":
            numDirect = 3

        newLoc = world[self.curLoc][numDirect]

        if newLoc == 4:
            if "Boat" == self.curItem:
                self.curLoc = newLoc
                locale[self.curLoc].count += 1
                locale[self.curLoc].visited = True
            else:
                print("You need a boat to go there.")
        
        elif newLoc is None:
            print("Wrong Way.\n")

        else:
            self.curLoc = newLoc

            if not locale[self.curLoc].visited:
                self.score += 5

            locale[self.curLoc].visited = True
            locale[self.curLoc].count += 1

        

    def search(self, locale):
        try:
            if locale[self.curLoc].item[0] != None:
                print("\n Look there's a", str(locale[self.curLoc].item), "\n")
                locale[self.curLoc].searched= True

            else:
                print("There is nothing here.\n")
        except:
            print("\nThere is nothing here.\n")

         
    def displayMenu(self,locale):
        print( "\n\n\t\t\tMain Menu\n"
                 "\t\t   ==================\n"+self.name+
                 "\nScore:" + str(self.score)+
                 "\nMoves Remaining: "+ str(self.moves) +
                 "\nCurrent Location: "+ locale[self.curLoc].afterVisit+
                 "\nInventory: "+ str(self.inventory) + 
                 "\nHealth: " +str(self.health)+
                 "\nStrength: "+str(self.strength)+
                 "\nSwiftness: " + str(self.swiftness)+
                 "\nCharisma: "+str(self.charisma)
               )
        
        

    def take(self, locale, items):
        item = self.cmd[5:].title()
        locItem = locale[self.curLoc].item

        if locItem != None:
            if locale[self.curLoc].searched:
                
                if item == locItem:
                    self.inventory[self.curLoc] = locItem
                    locale[self.curLoc].item = None
                    print(item, "has been added to your inventory.\n")

                else:
                    print("There is no", item, "\n")
            else:
                print("Search Around.\n")
        else:
            print("There is nothing to take.\n")
            
    def drop(self, locale):

        item = self.cmd[5:].title()
        inv = self.inventory 
        locItem = locale[self.curLoc].item                      
        if item in self.inventory:
            if locItem == None:
                print(item, "has been dropped and removed from your inventory.\n")
                locItem = item
                self.inventory[self.curLoc] = None
                locale[self.curLoc].item = locItem
            else:
                print("You can't drop this at the moment.\n")
        else:
            print("You don't have a", item)

    def equipItem(self):

        item = self.cmd[6:].title()
        if item in self.inventory:
            self.curItem = item
            print(item, "has been equiped.\n")

        else:
            print("You don't have", item ,"\n")

    def describe(self, locale):
        print(locale[self.curLoc].beforeVisit)

    def loseGame(self):
        print("You were killed by White Walkers and Westeros has been overrun..")
    
        
    def winGame(self):
        print("You took down the Night King and the undead Army!!!")
    
    
    def conclusion(self):
        print(    "\n==\n"
              "Copyright (c) Andrew DiBella       Andrew.DiBella1@marist.edu")


class Locale:

    def __init__(self, name, beforeVisit, afterVisit, item):

        self.name = name
        self.beforeVisit= beforeVisit
        self.afterVisit = afterVisit
        self.item = item
        self.count = 0
        self.visited = False
        self.searched = False
        self.hound = False



    def winterfell(self,player):
        while self.count == 1:

            sansaQues= input("You are greeted by Sansa Stark..\n Sansa: "+player.name +
                                 ", will you help us win this war?\nYes or no: ").lower()

            if sansaQues == "yes":
                print("\nWinterfell thanks you. We will win this together.")
                player.score += 5
                self.count += 1
                break
            elif sansaQues == "no":
                print("\nJust remember who the real enemy is..")
                self.count += 1
                break
            
    def houndBattle(self, player):
        def winBattle():
            print("\n You used your", player.curItem,"to take down the hound.\n")
            player.inventory.append("Armor")
            print("You took the Hounds armor.\n\n"
                    "Armor has been added to your inventory.")
            self.hound = True

        
        while True:
            response = input("The Hound challenges you to battle.\n"
                              "Do you accept? Yes/No: ")
            if response == "yes":
                if "Valyrian Steel Sword" == player.curItem and player.name == "Jon Snow":
                    winBattle()
                    break

                elif "Needle Sword" == player.curItem and player.name == "Arya":
                    winBattle()
                    break

                elif "Dragon Glass Dagger" == player.curItem and player.name == "Tyrion":
                    winBattle()
                    break

                elif "Oathkeeper Sword" == player.curItem and player.name == "Jaime":
                    winBattle()
                    break

                elif player.strength + player.swiftness > player.numDifficulty:
                    winBattle()
                    break
                else:
                    print("\nYou were killed by the Hound.")
                    player.conclusion()
                    sys.exit()
            

            elif response == "no":
                print("Hound: AHAHA, come back when your ready to fight.")
                break
            






        
