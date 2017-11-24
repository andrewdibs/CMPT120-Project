#classesZork.py
#Author Andrew DiBella
#Date 24 November 2017

class Player:


    def __init__(self, name, moves ):
        
        self.name = name
        self.moves = moves
        self.inventory = []
        self.curLoc = 0

    def move():
        pass


    def take():
        pass


    def drop():
        pass


    def look():
        pass


    def attack():
        pass

class Locale:

    def __init__(self, name, beforeVisit, afterVisit, item):

        self.name = name
        self.beforeVisit= beforeVisit
        self.afterVisit = afterVisit
        self.item = item
        self.visited = False
        self.searched = False
