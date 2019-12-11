import itertools, copy

theSystem = []

def getNum(numList, pos, mode):
    if(mode == 0):
        return numList[numList[pos]]
    elif(mode == 1):
        return numList[pos]

def putPos(numList, posVal, val):
    numList[numList[posVal]] = val


# 0          1         2       3       4        5         6       7
#input, inputReady, output, setting, lastOp, curCode, firstRun, numList

def runCode(num):
    inputVal = theSystem[num][0]
    inputReady = theSystem[num][1]
    settingVal = theSystem[num][3]
    curCode = theSystem[num][5]
    firstRun = theSystem[num][6]
    numList = theSystem[num][7]
    ret = 0
    while(True):
        instruction = numList[curCode]
        opCode = 0
        digits = [int(d) for d in str(instruction)]
        paramMode1 = 0
        paramMode2 = 0
        if(len(digits) == 4):
            opCode = digits[3]
            paramMode1 = digits[1]
            paramMode2 = digits[0]
        elif(len(digits) == 3):
            opCode = digits[2]
            paramMode1 = digits[0]
        else:
            opCode = instruction

        if(opCode == 99):
            theSystem[num][4] = 99
            break

        elif(opCode == 1):
            newVal = getNum(numList, curCode + 1, paramMode1) + getNum(numList, curCode + 2, paramMode2)
            putPos(numList, curCode + 3, newVal)
            curCode += 4

        elif(opCode == 2):
            newVal = getNum(numList, curCode + 1, paramMode1) * getNum(numList, curCode + 2, paramMode2)
            putPos(numList, curCode + 3, newVal)
            curCode += 4

        elif(opCode == 3):
            if(inputReady):
                if(firstRun):
                    numList[numList[curCode + 1]] = settingVal
                    firstRun = False
                    theSystem[num][6] = False
                else:
                    numList[numList[curCode + 1]] = inputVal
                    theSystem[num][1] = False
                    inputReady = False
                curCode += 2
            else:
                theSystem[num][5] = copy.deepcopy(curCode)
                break

        elif(opCode == 4):
            ret = getNum(numList, curCode + 1, paramMode1)
            theSystem[num][2] = copy.deepcopy(ret)
            if(num == 4):
                theSystem[0][0] = copy.deepcopy(ret)
                theSystem[0][1] = True
            else:
                theSystem[num + 1][0] = copy.deepcopy(ret)
                theSystem[num + 1][1] = True
            curCode += 2

        elif(opCode == 5):
            if(getNum(numList, curCode + 1, paramMode1) != 0):
                curCode = getNum(numList, curCode + 2, paramMode2)
            else:
                curCode += 3
                
        elif(opCode == 6):
            if(getNum(numList, curCode + 1, paramMode1) == 0):
                curCode = getNum(numList, curCode + 2, paramMode2)
            else:
                curCode += 3

        elif(opCode == 7):
            if(getNum(numList, curCode + 1, paramMode1) < getNum(numList, curCode + 2, paramMode2)):
                putPos(numList, curCode + 3, 1)
            else:
                putPos(numList, curCode + 3, 0)
            curCode += 4

        elif(opCode == 8):
            if(getNum(numList, curCode + 1, paramMode1) == getNum(numList, curCode + 2, paramMode2)):
                putPos(numList, curCode + 3, 1)
            else:
                putPos(numList, curCode + 3, 0)
            curCode += 4

        #print(curCode, ",", numList)

# 0          1         2       3       4        5         6       
#input, inputReady, output, setting, lastOp, curCode, firstRun, numList


file = open("C:/Users/akepley/Documents/AdventofCode2019/Day 7/input.txt", "r")
content = file.read()
initial = content.split(",")
for x in range(len(initial)):
    initial[x] = int(initial[x])
highest = 0
settings = list(itertools.permutations([5,6,7,8,9]))
for x in settings:
    theSystem = [
        [0, True, 0, 0, 0, 0, True],
        [0, True, 0, 0, 0, 0, True],
        [0, True, 0, 0, 0, 0, True],
        [0, True, 0, 0, 0, 0, True],
        [0, True, 0, 0, 0, 0, True]
    ]
    for y in theSystem:
        y.append(copy.deepcopy(initial))
    for y in range(5):
        theSystem[y][3] = x[y]
    repeat = True
    while(repeat):
        runCode(0)
        runCode(1)
        runCode(2)
        runCode(3)
        runCode(4)
        if(theSystem[4][4] == 99):
            repeat = False
            if(theSystem[4][2] > highest):
                highest = theSystem[4][2]
print(highest)