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

        



    def take(self):
        if locale[self.curLoc].searched:
            self.inventory.appends(locale[self.curLoc].item)
        else:
            print("There is nothing to take.\n")


    def drop(self):
        pass
    

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
