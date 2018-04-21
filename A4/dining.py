from pymongo import MongoClient
import threading
from time import sleep
import random

class Philosphoser(threading.Thread):
    connection = MongoClient("localhost", 27017)
    
    def readData(self, index):
        print "Reading data..."
        db = Philosphoser.connection.test.diniraw7
        cursor = db.find({"ph_no" : index})
        print str(cursor[0])
        
    def __init__(self, index, name, leftFork, rightFork):
        threading.Thread.__init__(self)
        self.index = index
        self.name = name
        self.leftFork = leftFork
        self.rightFork = rightFork
        
    def run(self):
        while(self.running == True):
            sleep(random.uniform(5, 15))
            print self.name + " is hungry"
            self.getFork()
            
    def getFork(self):
        fork1, fork2 = self.leftFork, self.rightFork
        while(self.running == True):
            fork1.acquire(True)
            lock = fork2.acquire(False)
            if lock : break
            fork1.release()
            print self.name + " swaps the forks"
            fork1, fork2 = fork2, fork1
        else:
            return
        
        self.dine()
        fork2.release()
        fork1.release()
        
    def dine(self):
        print self.name + " starts eating"
        self.readData(self.index)
        sleep(random.uniform(5, 15))
        print self.name + " finishes eating and goes back to thinking"
        
def Dining():
    fork = [threading.Lock() for i in range(5)]
    name = ["Chandler", "Joey", "Monica", "Rachael", "Ross"]
    phil = [Philosphoser(i, name[i], fork[i % 5], fork[(i + 1) % 5]) for i in range(5)]
    random.seed(1000)
    
    Philosphoser.running = True
    for p in phil:
        p.start()
    sleep(10)
    Philosphoser.running = False
    print "Finishing..."
    
Dining()