import random

def main():
    print(
    "\n----------------",
    "\nMATRIX GENERATOR",
    "\n----------------\n")
    inputs()
    print("\n")
    firstRow(width)
    allRows(height,width,probability)
    printRows()
    print("\n")

def inputs():
    global height
    ask=input("Height? ")
    if ask=='' or not ask.isdigit():
        height=15
    else:
        height=int(ask)-1
    global width
    ask=input("Width? ")
    if ask=='' or not ask.isdigit():
        width=120
    else:
        width=int(ask)
    global probability
    probability=0
    while probability<1 or probability>99:
        ask=input("Opacity? [1:Low - 99:High] ")
        if ask=='' or not ask.isdigit():
            probability=80
        else:
            probability=int(ask)
    global coloured
    global colour
    coloured=False
    ask=input("Colour? [y/n] ")
    if ask=="y":
        while ask not in "bg":
            ask=input("Blue or Green? [b/g] ")
        colour = ask
        coloured=True

def firstRow(width):
    row=""
    for w in range(width):
        row+=randomBinary()
    global rows
    rows={0:row}

def allRows(height,width,probability):
    index=0
    for h in range(height):
        row=""
        for w in range(width):
            if (rows[index][w]!=" "):
                if randomChance(probability):
                    row+=randomBinary()
                else:
                    row+=" "
            else:
                row+=" "
        if row.isspace():
            break
        index+=1
        rows[index]=row

def printRows():
    toPrint=[]
    if coloured:
        if colour is "b":
            pattern=blueColourPattern()
        else:
            pattern=greenColourPattern()
        for y in rows.keys():
            row=""
            for x in range(width):
                if x==0:
                    row+=pattern[x]+rows[y][x]
                row+=pattern[x]+rows[y][x:x+1]
            toPrint.append(row)
    else:
        for index in rows.keys():
            toPrint.append(rows[index])
    for row in toPrint:
        print(row)

def randomBinary():
    return str(random.randint(0,1))

def randomChance(probability):
    number=random.randint(1,100)
    if number>probability:
        return False
    return True

def randomBlueColours():
    number=random.randint(0,7)
    if number==0:
        return "\033[0;94m"
    elif number==1:
        return "\033[0;96m"
    elif number==2:
        return "\033[0;34m"
    elif number==3:
        return "\033[0;36m"
    elif number==4:
        return "\033[1;94m"
    elif number==5:
        return "\033[1;96m"
    elif number==6:
        return "\033[1;34m"
    elif number==7:
        return "\033[1;36m"

def blueColourPattern():
    pattern={}
    for w in range(width):
        pattern[w]=randomBlueColours()
    return pattern

def randomGreenColours():
    number=random.randint(0,7)
    if number==0:
        return "\033[0;92m"
    elif number==1:
        return "\033[0;96m"
    elif number==2:
        return "\033[0;32m"
    elif number==3:
        return "\033[0;36m"
    elif number==4:
        return "\033[1;92m"
    elif number==5:
        return "\033[1;96m"
    elif number==6:
        return "\033[1;32m"
    elif number==7:
        return "\033[1;36m"

def greenColourPattern():
    pattern={}
    for w in range(width):
        pattern[w]=randomGreenColours()
    return pattern

main()