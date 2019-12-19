import copy




#0           1            2            3               4
#input     output      curCode     lastOpCode       relbase
programList = [[],[],0,0,0]

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

        # print("opCode: ", opCode)

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
            if(len(programList[0]) == 0):
                break
            takeInput = programList[0].pop(0)
            putPos(numList, curCode + 1, takeInput, relBase, paramMode1)
            curCode += 2

        elif(opCode == 4):
            # print(getNum(numList, curCode + 1, paramMode1, relBase))
            programList[1].append(getNum(numList, curCode + 1, paramMode1, relBase))
            curCode += 2
            programList[2] = curCode
            # break
        
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

        
def queryPoint(x, y):
    global programList
    global initial
    saveInitial = copy.deepcopy(initial)
    saveProgramList = copy.deepcopy(programList)
    programList[0].append(x)
    programList[0].append(y)
    runCode(initial)
    ret = programList[1][0]
    initial = copy.deepcopy(saveInitial)
    programList = copy.deepcopy(saveProgramList)
    return ret


#0           1            2            3          4
#input     output      curCode     lastOpCode   relBase


file = open("Day 19/input.txt", "r")
content = file.read()
initial = content.split(",")
for x in range(len(initial)):
    initial[x] = int(initial[x])
for x in range(10000):
    initial.append(0)
count = 0
count = 0
curVal = 1447
last = 0
notFound = True
# while(notFound):
for x in range(1000,2000):
    val = queryPoint(x, curVal)
    if(last == 0 and val == 1):
        print(x, curVal + 1)
        # if(queryPoint(x+100, curVal-100) == 1):
        #     print((x, curVal-100))
        #     notFound = False
        for a in range(curVal-99, curVal + 1):
            for b in range(x, x + 100):
                val = queryPoint(b, a)
                print(val, end=" ")
            print()
        break
    last = val
    # curVal += 1
