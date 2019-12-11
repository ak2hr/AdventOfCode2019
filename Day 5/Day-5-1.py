def getNum(numList, pos, mode):
    if(mode == 0):
        return numList[numList[pos]]
    elif(mode == 1):
        return numList[pos]

def putPos(numList, posVal, val):
    numList[numList[posVal]] = val

def runCode(numList):
    curCode = 0
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
            takeInput = int(input("Enter input code: "))
            numList[numList[curCode + 1]] = takeInput
            curCode += 2

        elif(opCode == 4):
            print(getNum(numList, curCode + 1, paramMode1))
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

        

file = open("C:/Users/akepley/Desktop/input.txt", "r")
content = file.read()
initial = content.split(",")
for x in range(len(initial)):
    initial[x] = int(initial[x])
runCode(initial)