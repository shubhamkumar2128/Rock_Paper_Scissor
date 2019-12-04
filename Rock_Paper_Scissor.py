#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

class RPS:
    def start(self):
        print("1 for ROCK\n2 for Paper\n3 for Scissors")
        choice = int(input("Please Select = "))
        self.inputAction(choice)
        
    def inputAction(self, ch):
        if ch == 1:
            self.printValues(ch,"User")
            self.match(ch)
        elif ch == 2:
            self.printValues(ch,"User")
            self.match(ch)
        elif ch == 3:
            self.printValues(ch,"User")
            self.match(ch)
        else: print("Invalid")

    def printValues(self, x,playermove):
        if x == 1:   print(playermove+" selected rock")
        elif x == 2: print(playermove+" selected paper")
        elif x == 3: print(playermove+" selected Scissors")

    def computerMove(self):
        x = random.randint(1, 3)
        self.printValues(x,"Computer")
        return x

    def match(self, user):
        cmp = self.computerMove()
        check=self.check(user, cmp)
        if check==True:     print("user wins")
        elif check==False:  print("computer wins")
        else:               print("Draw Game")

    def check(self, user, cmp):

            if user == 1:
                if cmp == 3: return True
                elif cmp == 2: return False
            elif user == 2:
                if cmp == 1: return True
                elif cmp == 3: return False
            elif user == 3:
                if cmp == 2: return True
                elif cmp == 1: return False


obj = RPS().start()

