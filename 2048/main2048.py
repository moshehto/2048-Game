import pgzrun
import random
from grid import *

WIDTH = 500
HEIGHT = 500
brow1 = []
brow2 = []
brow3 = []
brow4 = []



row1 = [0,0,0,0]
row2 = [0,0,0,0]
row3 = [0,0,0,0]
row4 = [0,0,0,0]

# left

loser = False

options = [(1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (2,3), (3,0), (3,1), (3,2), (3,3), (4,0), (4,1), (4,2), (4,3)]

while len(options) > 0:
    n = random.randint(0, len(options) - 1)
    row = options[n][0]
    col = options[n][1]
    if row == 1:
        if row1[col] == 0:
            row1[col] = 2
            break
    elif row == 2:
        if row2[col] == 0:
            row2[col] = 2
            break
    elif row == 3:
        if row3[col] == 0:
            row3[col] = 2
            break
    elif row == 4:
        if row4[col] == 0:
            row4[col] = 2
            break
for i in range(4):
    brow1.append(Actor(str(row1[i]), topleft=(125*i,0)))
    brow2.append(Actor(str(row2[i]), topleft=(125*i,125)))
    brow3.append(Actor(str(row3[i]), topleft=(125*i,250)))
    brow4.append(Actor(str(row4[i]), topleft=(125*i,375)))
        

    
def draw():
    screen.blit('background', (0, 0))

    
    for i in range(4):
        brow1[i].draw()
        brow2[i].draw()
        brow3[i].draw()
        brow4[i].draw()
    
    if loser == True:
        screen.draw.text(str("Game Over!"), (130, 220), fontsize = 64)
    



def update():
    pass


def on_key_down():
    



    if not loser:

       
        if keyboard.down:
            ShiftDown(row1, row2, row3, row4)
            newTiles()
            updateBoard()
            

        
        
        if keyboard.up:
            ShiftUp(row1, row2, row3, row4)
            newTiles()
            updateBoard()

            

           
        if keyboard.right:
            ShiftRight(row1, row2, row3, row4)
            newTiles()
            updateBoard()
            
        if keyboard.left:
            ShiftLeft(row1, row2, row3, row4)
            newTiles()
            updateBoard()
            

    
        



def updateBoard():
    global brow1, brow2, brow3, brow4
    brow1 = []
    brow2 = []
    brow3 = []
    brow4 = []
    for i in range(4):
            brow1.append(Actor(str(row1[i]), topleft=(125*i,0)))
            brow2.append(Actor(str(row2[i]), topleft=(125*i,125)))
            brow3.append(Actor(str(row3[i]), topleft=(125*i,250)))
            brow4.append(Actor(str(row4[i]), topleft=(125*i,375)))

    
def newTiles():
    global options, loser
    options = [(1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (2,3), (3,0), (3,1), (3,2), (3,3), (4,0), (4,1), (4,2), (4,3)]
    
    while len(options) > 0:
        n = random.randint(0, len(options) - 1)
        row = options[n][0]
        col = options[n][1]
        if row == 1:
            if row1[col] == 0:
                row1[col] = 2
                break
        elif row == 2:
            if row2[col] == 0:
                row2[col] = 2
                break
        elif row == 3:
            if row3[col] == 0:
                row3[col] = 2
                break
        elif row == 4:
            if row4[col] == 0:
                row4[col] = 2
                break
        del options[n]
        
        
    if len(options) == 0:
        loser = True
    
        


pgzrun.go()