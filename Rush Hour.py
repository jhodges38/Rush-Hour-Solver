#!/usr/bin/env python
# coding: utf-8

# Rush Hour Solver

# In[14]:


from time import sleep
from collections import deque
import copy
from colored import fg, attr
import itertools as it

CarColors = ["CB", "CA", "C9", "C8", "C7", "C6", "C5", "C4", "C3","C2","C1", "RC"]
TruckColors = ["T4", "T3", "T2", "T1"]
MoveWords = ['one', 'two', 'three', 'four']

class Vehicle:
    
    def __init__(self, orientation, bumperx, bumpery, V_Type):
        self.orientation = orientation
        self.bumperx = bumperx
        self.bumpery = bumpery
        self.V_Type = V_Type
        if self.V_Type == "Car":
            self.length = 2
            self.color = CarColors[-1]
        elif self.V_Type == "Truck":
            self.length = 3
            self.color = TruckColors[-1]
                
    def __str__(self):
        return self.color + self.orientation + "(" + self.bumperx + "," + self.bumpery + ")"



class Board:
    
    def __init__(self):
        self.board = [["--" for num in range(6)]for nums in range(6)]
        self.vehicles = {}
    
    def vehicle_add(self, Vehicle, coloring):
        if Vehicle.V_Type == "Car":
            self.vehicles[coloring + CarColors.pop() + attr('reset')] = Vehicle
        else:
            self.vehicles[coloring + TruckColors.pop() + attr('reset')] = Vehicle
        if Vehicle.orientation == "h":
            for cell in range(Vehicle.length):
                self.board[Vehicle.bumpery][Vehicle.bumperx + cell] = coloring + Vehicle.color + attr('reset')
        else:
            for cell in range(Vehicle.length):
                self.board[Vehicle.bumpery + cell][Vehicle.bumperx] = coloring + Vehicle.color + attr('reset')

    def get_board(self):
        for row in range(6):
            for column in range(6):
                if column == 5:
                    print(self.board[row][column])          
                else:
                    print(self.board[row][column], end = ' ')
    

def intro():
    print("Welcome to Rush Hour!")
    print()
    sleep(1)

def setupauto():
    global B, vehicle
    
    B = Board()
    B.get_board()
    valid = False
    print()
    
    print("It's time to place your vehicles:")
    print()
    
    while valid == False:
        try:
            redx = int(input("Let's start with the red car. What position would you like the rear bumper to be in? Enter an integer 1-5."))-1
        except:
            redx = -1
        if 0 <= redx <= 4:
            vehicle = Vehicle("h",redx,2,"Car")
            B.vehicle_add(vehicle, fg(1))
            valid = True
        else:
            valid = False
        
    
    print()
    B.get_board()
    print()
            

def create_car():
    global B, vehicle
    
    valid = False
    
    while valid == False:
        valid = True
        try:
            bumperx = int(input("What horizontal position would you like the rear bumper to be in? Enter an integer 1-6."))-1
            bumpery = int(input("What vertical position would you like the rear bumper to be in? Enter an integer 1-6."))-1
        except:
            bumperx = -1
            bumpery = -1
        print("What is the orientation of your car?")
        orientation = input("h) Horizontal  v) Vertical ")
        print(fg(244) + "1. Grey" + attr('reset')+ "\n"+ fg(208) + "2. Orange" + attr('reset')+ "\n"+ fg(211) + "3. Pink" + attr('reset')+ "\n"+ fg(99) + "4. Purple" + attr('reset')+ "\n"+ fg(29) + "5. Green" + attr('reset')+ "\n"+ fg(120) + "6. Light Green" + attr('reset')+ "\n"+ fg(106) + "7. Pea Green" + attr('reset')+ "\n"+ fg(95) + "8. Brown" + attr('reset')+ "\n"+ fg(223) + "9. Beige" + attr('reset')+ "\n"+ fg(227) + "10. Light Yellow" + attr('reset')+ "\n"+ fg(81) + "11. Light Blue" + attr('reset')+ "\n")
        try:
            colornum = int(input("Enter the color of your car 1 through 11:"))
        except:
            colornum = -1
        if colornum == 1:
            colorcode = fg(244)
        elif colornum == 2:
            colorcode = fg(208)
        elif colornum == 3:
            colorcode = fg(211)
        elif colornum == 4:
            colorcode = fg(99)
        elif colornum == 5:
            colorcode = fg(29)
        elif colornum == 6:
            colorcode = fg(120)
        elif colornum == 7:
            colorcode = fg(106)
        elif colornum == 8:
            colorcode = fg(95)
        elif colornum == 9:
            colorcode = fg(223)
        elif colornum == 10:
            colorcode = fg(227)
        elif colornum == 11:
            colorcode = fg(81)
        else:
            valid = False
            
        if orientation == "h":
            if 0 <= bumperx <= 4 and 0 <= bumpery <= 5 and B.board[bumpery][bumperx] == "--" and B.board[bumpery][bumperx + 1] == "--":
                vehicle = Vehicle(orientation,bumperx,bumpery,"Car")
                B.vehicle_add(vehicle, colorcode)
            else:
                valid = False
        elif orientation == "v":
            if 0 <= bumperx <= 5 and 0 <= bumpery <= 4 and B.board[bumpery][bumperx] == "--" and B.board[bumpery + 1][bumperx] == "--":
                vehicle = Vehicle(orientation,bumperx,bumpery,"Car")
                B.vehicle_add(vehicle, colorcode)
            else:
                valid = False        
        else:
            valid = False
            
    print()
    B.get_board()
    print()
              
    
def create_truck():
    global B, vehicle
    
    valid = False
    
    while valid == False:
        valid = True
        try:
            bumperx = int(input("What horizontal position would you like the rear bumper to be in? Enter an integer 1-6."))-1
            bumpery = int(input("What vertical position would you like the rear bumper to be in? Enter an integer 1-6."))-1
        except:
            bumperx = -1
            bumpery = -1
        print("What is the orientation of your truck?")
        orientation = input("h) Horizontal  v) Vertical ")
        print(fg(183) + "1. Light Purple" + attr('reset') + "\n" + fg(220) + "2. Yellow" + attr('reset')+ "\n"+ fg(33) + "3. Blue" + attr('reset')+ "\n"+ fg(49) + "4. Teal"+ attr('reset') + "\n")
        try:
            colornum = int(input("Enter the color of your truck 1 through 4:"))
        except:
            colornum = -1 
        if colornum == 1:
            colorcode = fg(183)
        elif colornum == 2:
            colorcode = fg(220)
        elif colornum == 3:
            colorcode = fg(33)
        elif colornum == 4:
            colorcode = fg(49)
        else:
            valid = False
        
        if orientation == "h":
            if 0 <= bumperx <= 3 and 0 <= bumpery <= 5 and B.board[bumpery][bumperx] == "--" and B.board[bumpery][bumperx + 1] == "--" and B.board[bumpery][bumperx + 2] == "--":
                vehicle = Vehicle(orientation,bumperx,bumpery,"Truck")
                B.vehicle_add(vehicle, colorcode)
            else:
                valid = False
        elif orientation == "v":
            if 0 <= bumperx <= 5 and 0 <= bumpery <= 3 and B.board[bumpery][bumperx] == "--" and B.board[bumpery + 1][bumperx] == "--" and B.board[bumpery + 2][bumperx] == "--":
                vehicle = Vehicle(orientation,bumperx,bumpery,"Truck")
                B.vehicle_add(vehicle, colorcode)
            else:
                valid = False        
        else:
            valid = False
            
    print()
    B.get_board()
    print()
    

def game_exit():
    print ('Thanks for playing!')
    sys.exit()

def play():
    global B
    
    tried = set()
    origflatten = [item for sublist in B.board for item in sublist]
    tried.add(hash(tuple(origflatten)))
    paths = deque()
    paths.appendleft([B.board])
    move = 0
    moves = deque([[""]])
    currentboards = deque()
    currentboards.appendleft(B)

    while len(currentboards) != 0:
        for k, v in currentboards[0].vehicles.items():
            if v.orientation == "h":
                back = 0
                forward = 0
                while v.bumperx + back >= 1:
                    if currentboards[0].board[v.bumpery][v.bumperx + back - 1] == "--":
                        back -= 1
                    else: 
                        break
                while v.bumperx + v.length + forward <= 5:
                    if currentboards[0].board[v.bumpery][v.bumperx + v.length + forward] == "--":
                        forward += 1 
                    else: 
                        break 
                for choice in it.chain(range(-1, back - 1, -1), range(1, forward + 1)):
                    testboard = copy.deepcopy(currentboards[0])
                    plurality = 'spaces' if abs(choice) > 1 else 'space'
                    if choice < 0:
                        direction = 'left'
                        for slide in range(-1, choice - 1, -1):
                            testboard.board[v.bumpery][v.bumperx + slide] = k
                            testboard.board[v.bumpery][v.bumperx + v.length + slide] = "--"
                    else:
                        direction = 'right'
                        for slide in range(1, choice + 1):
                            testboard.board[v.bumpery][v.bumperx + v.length + slide - 1] = k
                            testboard.board[v.bumpery][v.bumperx + slide - 1] = "--"                            
                    flatten = [item for sublist in testboard.board for item in sublist]
                    if not hash(tuple(flatten)) in tried:
                        tried.add(hash(tuple(flatten)))
                        testboard.vehicles[k].bumperx += choice
                        currentboards.append(testboard)
                        paths.append(paths[0] + [testboard.board])
                        moves.append(moves[0] + [k + " moves " + direction + " " + MoveWords[abs(choice) - 1] + " " + plurality])
                        if testboard.board[2][5] == fg(1)+"RC"+attr('reset'):
                            print("Solved!")
                            for pboard in paths[-1]:
                                print(moves[-1][move])
                                print()
                                for row in range(6):
                                    for column in range(6):
                                        if column == 5:
                                            print(pboard[row][column])          
                                        else:
                                            print(pboard[row][column], end = ' ')
                                print()
                                move += 1
                            return
                    
            elif v.orientation == "v":
                back = 0
                forward = 0
                while v.bumpery + back >= 1:
                    if currentboards[0].board[v.bumpery + back - 1][v.bumperx] == "--":
                        back -= 1 
                    else:
                        break
                while v.bumpery + v.length + forward <= 5:
                    if currentboards[0].board[v.bumpery + v.length + forward][v.bumperx] == "--":
                        forward += 1 
                    else:
                        break
                for choice in it.chain(range(-1, back - 1, -1), range(1, forward + 1)):
                    testboard = copy.deepcopy(currentboards[0])
                    plurality = 'spaces' if abs(choice) > 1 else 'space'
                    if choice < 0:
                        direction = 'up'
                        for slide in range(-1, choice - 1, -1):
                            testboard.board[v.bumpery + slide][v.bumperx] = k
                            testboard.board[v.bumpery + v.length + slide][v.bumperx] = "--"
                    else:
                        direction = 'down'
                        for slide in range(1, choice + 1):
                            testboard.board[v.bumpery + v.length + slide - 1][v.bumperx] = k
                            testboard.board[v.bumpery + slide - 1][v.bumperx] = "--"                            
                    flatten = [item for sublist in testboard.board for item in sublist]
                    if not hash(tuple(flatten)) in tried:
                        tried.add(hash(tuple(flatten)))
                        testboard.vehicles[k].bumpery += choice
                        currentboards.append(testboard)
                        paths.append(paths[0] + [testboard.board])
                        moves.append(moves[0] + [k + " moves " + direction + " " + MoveWords[abs(choice) - 1] + " " + plurality])
                        if testboard.board[2][5] == fg(1)+"RC"+attr('reset'):
                            print("Solved!")
                            for pboard in paths[-1]:
                                print(moves[-1][move])
                                print()
                                for row in range(6):
                                    for column in range(6):
                                        if column == 5:
                                            print(pboard[row][column])          
                                        else:
                                            print(pboard[row][column], end = ' ')
                                print()
                                move += 1
                            return
                        
        currentboards.popleft()
        paths.popleft()
        moves.popleft()
    

def setupplayer():
    
    place = "a"
    
    while place != "p":
        print("Would you like to place a Car, a Truck, or are you ready to play?")
        print()
        place = input("c) Car   t) Truck   p) Play   e) Exit ")
        if place == "c":
            create_car()
        elif place == "t":
            create_truck()
        elif place == "e":
            game_exit()
        elif place == "p":
            play()
        else:
            print("Please enter a valid option")
            
    


# In[15]:


intro()
setupauto()
setupplayer()



# In[ ]:




