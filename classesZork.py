#classesZork.py
#Author Andrew DiBella
#Date 24 November 2017

class Player:


    def __init__(self, name, moves ):
        
        self.name = name
        self.moves = moves
        self.inventory = []
        self.curLoc = 0
        self.cmd = ""
        self.score = 0
        
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

        if newLoc is None:
            print("Wrong Way.\n")

        else:
            self.curLoc = newLoc

            if not locale[self.curLoc].visited:
                self.score += 5

            locale[self.curLoc].visited = True
            locale[self.curLoc].count += 1

        

    def search(self, locale):
        if locale[self.curLoc].item != None:
            print("\n Look there's a", locale[self.curLoc].item, "\n")
            locale[self.curLoc].searched= True
        else:
            print("\nThere is nothing here.\n")

         
    def displayMenu(self,locale):
        print( "\n\n\t\t\tMain Menu\n"
                 "\t\t   ==================\n"+self.name+
                 "\nScore:" + str(self.score)+
                 "\nMoves Remaining: "+ str(self.moves) +
                 "\nCurrent Location: "+ locale[self.curLoc].afterVisit+
                 "\nInventory:"+ str(self.inventory) + "\n\n")
        
        

    def take(self, locale, items):
        if locale[self.curLoc].searched:
            self.inventory.append(locale[self.curLoc].item)
            
            print("\n", locale[self.curLoc].item, "has been added to your inventory\n")
            
            items[self.curLoc] = None
            locale[self.curLoc].item = None

            
        else:
            print("There is nothing to take.\n")


##    def drop(self, locale):
##        for index in range(0, 10):
##
##            if self.cmd[5:].capitilize() == locale[index].item:
##                self.inventory.remove(item)
##                print(item, "has been dropped and removed from your inventory.\n")
##                locale[index].item = 
##    

    def describe(self):
        pass


    def attack(self):
        pass

class Locale:

    def __init__(self, name, beforeVisit, afterVisit, item):

        self.name = name
        self.beforeVisit= beforeVisit
        self.afterVisit = afterVisit
        self.item = item
        self.count = 0
        self.visited = False
        self.searched = False
