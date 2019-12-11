#0           1            2            3            4           5
#input     output      curCode     lastOpCode     facing     relbase
programList = [0,0,0,0,"U",0]

def getNum(numList, pos, mode, relBase):
    if(mode == 0):
        return numList[numList[pos]]
    elif(mode == 1):
        return numList[pos]
    elif(mode == 2):
        return numList[numList[pos] + relBase]

def putPos(numList, posVal, val, relBase, paramMode):
    if(paramMode == 2):
        numList[numList[posVal] + relBase] = val
    else:
        numList[numList[posVal]] = val

def runCode(numList):
    curCode = programList[2]
    relBase = programList[5]
    while(True):
        instruction = numList[curCode]
        opCode = 0
        digits = [int(d) for d in str(instruction)]
        paramMode1 = 0
        paramMode2 = 0
        paramMode3 = 0
        if(len(digits) == 4):
            opCode = digits[3]
            paramMode1 = digits[1]
            paramMode2 = digits[0]
        elif(len(digits) == 3):
            opCode = digits[2]
            paramMode1 = digits[0]
        elif(len(digits) == 5):
            opCode = digits[4]
            paramMode1 = digits[2]
            paramMode2 = digits[1]
            paramMode3 = digits[0]
        else:
            opCode = instruction

        if(opCode == 99):
            programList[3] = 99
            break

        elif(opCode == 1):
            newVal = getNum(numList, curCode + 1, paramMode1, relBase) + getNum(numList, curCode + 2, paramMode2, relBase)
            putPos(numList, curCode + 3, newVal, relBase, paramMode3)
            curCode += 4

        elif(opCode == 2):
            newVal = getNum(numList, curCode + 1, paramMode1, relBase) * getNum(numList, curCode + 2, paramMode2, relBase)
            putPos(numList, curCode + 3, newVal, relBase, paramMode3)
            curCode += 4

        elif(opCode == 3):
            takeInput = programList[0]
            putPos(numList, curCode + 1, takeInput, relBase, paramMode1)
            curCode += 2

        elif(opCode == 4):
            #print(getNum(numList, curCode + 1, paramMode1, relBase))
            programList[1] = getNum(numList, curCode + 1, paramMode1, relBase)
            curCode += 2
            programList[2] = curCode
            break
        
        elif(opCode == 5):
            if(getNum(numList, curCode + 1, paramMode1, relBase) != 0):
                curCode = getNum(numList, curCode + 2, paramMode2, relBase)
            else:
                curCode += 3
                
        elif(opCode == 6):
            if(getNum(numList, curCode + 1, paramMode1, relBase) == 0):
                curCode = getNum(numList, curCode + 2, paramMode2, relBase)
            else:
                curCode += 3

        elif(opCode == 7):
            if(getNum(numList, curCode + 1, paramMode1, relBase) < getNum(numList, curCode + 2, paramMode2, relBase)):
                putPos(numList, curCode + 3, 1, relBase, paramMode3)
            else:
                putPos(numList, curCode + 3, 0, relBase, paramMode3)
            curCode += 4

        elif(opCode == 8):
            if(getNum(numList, curCode + 1, paramMode1, relBase) == getNum(numList, curCode + 2, paramMode2, relBase)):
                putPos(numList, curCode + 3, 1, relBase, paramMode3)
            else:
                putPos(numList, curCode + 3, 0, relBase, paramMode3)
            curCode += 4

        elif(opCode == 9):
            relBase += getNum(numList, curCode + 1, paramMode1, relBase)
            programList[5] = relBase
            curCode += 2

        
#0           1            2            3            4
#input     output      curCode     lastOpCode     facing


file = open("C:/Users/Andrew/Desktop/input.txt", "r")
content = file.read()
initial = content.split(",")
for x in range(len(initial)):
    initial[x] = int(initial[x])
for x in range(10000):
    initial.append(0)
curX = 0
curY = 0
mySet = {1}
mySet.clear()
paintDict = {}
while(True):
    #set input bsaed on current position (default is black)
    if(len(mySet) == 0):
        programList[0] = 1
    elif((curX, curY) not in paintDict.keys()):
        programList[0] = 0
    else:
        programList[0] = paintDict[(curX, curY)]
    #run code with that input to get color to paint space
    runCode(initial)
    #add painted point to set of points that have been painted
    mySet.add((curX, curY))
    #add point to dictionary to keep track of what color it was painted
    paintDict[(curX, curY)] = programList[1]
    #break if program done
    if(programList[3] == 99):
        break
    #run code again to get turn instructions
    runCode(initial)
    #determine new direction and new point to be in
    direction = programList[4]
    output = programList[1]
    if((direction == "U" and output == 0) or (direction == "D" and output == 1)):
        programList[4] = "L"
        curX -= 1
    elif((direction == "U" and output == 1) or (direction == "D" and output == 0)):
        programList[4] = "R"
        curX += 1
    elif((direction == "L" and output == 1) or (direction == "R" and output == 0)):
        programList[4] = "U"
        curY += 1
    elif((direction == "L" and output == 0) or (direction == "R" and output == 1)):
        programList[4] = "D"
        curY -= 1
    if(programList[3] == 99):
        break
maxX = 0
minX = 0
maxY = 0
minY = 0
for x in paintDict.keys():
    if(x[0] > maxX):
        maxX = x[0]
    if(x[0] < minX):
        minX = x[0]
    if(x[1] > maxY):
        maxY = x[1]
    if(x[1] < minY):
        minY = x[1]
print(minX, ", ", maxX)
print(minY, ", ", maxY)
myList = []
for y in range(6):
    tempList = []
    for x in range(maxX):
        tempList.append(".")
    myList.append(tempList)
for x in paintDict:
    if(paintDict[x] == 1):
        print(x)
        myList[abs(x[1])][x[0]] = "#"
for x in myList:
    print(x)