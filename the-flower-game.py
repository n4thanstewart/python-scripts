import random
import time

def title():
    print(
        "\n---------------",
        "\nTHE FLOWER GAME",
        "\n---------------",
        "\n",
        "\nThe only play permitted in the game is the arrangement of the initial flowers...",
        "\n"
        )

def sourceMaterialQuote():
    index=random.randint(0,3)
    quotes=[
        "\"let it be played upon an infinite two-dimensional grid of flowers...\"",
        "\"changeless blocks, stoic as iron, and beacons and whirling pulsars...\"",
        "\"a seed resembles the star that fed the flower and all the life that made it...\"",
        "\"and in time the gardener became vexed...\""
    ]
    return "\n\033[94m"+quotes[index]+"\n\033[m"

global size
size=35

def customise():
    global size
    while True:
        ask=input("Grid size? [1-100] ")
        if ask=='' or not ask.isdigit():
            continue
        elif 1<=int(ask) and int(ask)<=100:
            size=int(ask)
            break
        else:
            continue

def binaryChance():
    return random.randint(0,1)

def randomiseGrid():
    y=[]
    for h in range(size):
        x=[]
        for w in range(size):
            x.append(binaryChance())
        y.append(x)
    return y

def observer(grid,coordinate):
    x=coordinate[1]
    y=coordinate[0]
    left=right=above=below=None
    if x!=0:
        left=grid[y][x-1]
    if x!=size-1:
        right=grid[y][x+1]
    if y!=0:
        above=grid[y-1][x]
    if y!=size-1:
        below=grid[y+1][x]
    return [left,right,above,below]

def gardener(flower,observations):
    if flower==1:
        alive=True
    else:
        alive=False
    livingNeighbours=0
    deadNeighbours=0
    for neighbour in observations:
        if neighbour is None:
            continue
        if neighbour==1:
            livingNeighbours+=1
        else:
            deadNeighbours+=1
    # Rule One
    if alive and livingNeighbours<2:
        return 0
    # Rule Two
    if alive and (livingNeighbours==2 or livingNeighbours==3):
        return flower
    # Rule Three
    if alive and 3<livingNeighbours:
        return 0
    # Rule Four
    if not alive and livingNeighbours==3:
        return 1
    return flower

def winnower(grid):
    newGrid=[]
    for y in range(size):
        newRow=[]
        for x in range(size):
            observations=observer(grid,[y,x])
            newRow.append(gardener(grid[y][x],observations))
        newGrid.append(newRow)
    if grid==newGrid:
        return None
    return newGrid

def printFlowerGrid(grid):
    print("\n")
    gridToPrint=""
    for y in range(size):
        rowToPrint=""
        for x in range(size):
            flower=grid[y][x]
            if flower==1:
                rowToPrint+=" \033[92m❀\033[m "
            else:
                rowToPrint+=" \033[30mx\033[m "
        gridToPrint+="\n"+rowToPrint
    print(gridToPrint)
                
def theFlowerGame():
    grid=randomiseGrid()
    turn=0
    while True:
        printFlowerGrid(grid)
        grid=winnower(grid)
        if grid is None:
            break
        time.sleep(1)
        turn+=1
        if turn==20:
            break

def execLoop():
    while True:
        print("Grid size:\033[94m",size,"\033[m")
        ask=input("Enter 'c' to customise, or any other key to begin the game ")
        if ask=='c':
            customise()
        theFlowerGame()
        time.sleep(1)
        print(sourceMaterialQuote())
        time.sleep(2.5)
        ask=input("Start again? [y/n] ")
        if ask=='y':
            continue
        else:
            break

# Game Start
title()
time.sleep(2)
execLoop()