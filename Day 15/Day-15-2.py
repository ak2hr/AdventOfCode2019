import random, copy

#0           1            2            3               4
#input     output      curCode     lastOpCode       relbase
programList = [0,0,0,0,0]
initial = []


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
    relBase = programList[4]
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
            programList[4] = relBase
            curCode += 2

        
#0           1            2            3          4
#input     output      curCode     lastOpCode   relBase

stepsList = {}

def findKnown(point, steps):
    global initial
    global programList
    stepsList[point] = steps
    saveInitial = copy.deepcopy(initial)
    saveProgramList = copy.deepcopy(programList)
    up = (point[0], point[1] + 1)
    down = (point[0], point[1] - 1)
    left = (point[0] + 1, point[1])
    right = (point[0] - 1, point[1])
    if(up not in stepsList):
        programList[0] = 1
        runCode(initial)
        if(programList[1] != 0):
            findKnown(up, steps + 1)
    initial = copy.deepcopy(saveInitial)
    programList = copy.deepcopy(saveProgramList)
    if(down not in stepsList):
        programList[0] = 2
        runCode(initial)
        if(programList[1] != 0):
            findKnown(down, steps + 1)
    initial = copy.deepcopy(saveInitial)
    programList = copy.deepcopy(saveProgramList)
    if(left not in stepsList):
        programList[0] = 3
        runCode(initial)
        if(programList[1] != 0):
            findKnown(left, steps + 1)
    initial = copy.deepcopy(saveInitial)
    programList = copy.deepcopy(saveProgramList)
    if(right not in stepsList):
        programList[0] = 4
        runCode(initial)
        if(programList[1] != 0):
            findKnown(right, steps + 1)
    
    



file = open("Day 15/input.txt", "r")
content = file.read()
initial = content.split(",")
for x in range(len(initial)):
    initial[x] = int(initial[x])
for x in range(10000):
    initial.append(0)
curX = 0
curY = 0
wallList = {0}
wallList.remove(0)
stepsList = {}
stepsList[str((0,0))] = 0
start = (0,0)
end = (0,0)
current = (0,0)
steps = 0
while(True):
    programList[0] = random.randint(1,4)
    runCode(initial)
    if(programList[0] == 1):
        if(programList[1] == 0):
            wallList.add((curX, curY + 1))
        else:    
            curY += 1
    elif(programList[0] == 2):
        if(programList[1] == 0):
            wallList.add((curX, curY - 1))
        else:    
            curY -= 1
    elif(programList[0] == 3):
        if(programList[1] == 0):
            wallList.add((curX - 1, curY))
        else:    
            curX -= 1
    elif(programList[0] == 4):
        if(programList[1] == 0):
            wallList.add((curX + 1, curY))
        else:    
            curX += 1
    current = (curX,curY)
    if(str(current) not in stepsList):
        steps += 1
        stepsList[str(current)] = steps
    else:
        steps = stepsList[str(current)]
    if(programList[1] == 2):
        end = current
        break
findKnown(end, 0)
max = 0
for x in stepsList:
    if(stepsList[x] > max):
        max = stepsList[x]
print(max)