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
        width=80
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

main()