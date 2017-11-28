#classesZork.py
#Author Andrew DiBella
#Date 24 November 2017

class Player:


    def __init__(self, name, moves ):
        
        self.name = name
        self.moves = moves
        self.inventory = [None,None,None,None,None,None,None,None,None,None,None,None]
        self.curLoc = 0
        self.cmd = ""
        self.score = 0
        self.curItem = ""
        
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
                 "\nInventory:"+ str(self.inventory) + "\n\n")
        
        

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

    def describe(self):
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
