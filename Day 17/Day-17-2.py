#0           1            2            3               4
#input     output      curCode     lastOpCode       relbase
programList = [0,0,0,0,0]

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
            programList[3] = 3
            programList[2] = curCode
            break

        elif(opCode == 4):
            val = getNum(numList, curCode + 1, paramMode1, relBase)
            print(chr(val), end=" ")
            programList[1] = getNum(numList, curCode + 1, paramMode1, relBase)
            curCode += 2
            programList[2] = curCode
            programList[3] = 4
        
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


file = open("Day 17/input.txt", "r")
content = file.read()
initial = content.split(",")
for x in range(len(initial)):
    initial[x] = int(initial[x])
for x in range(10000):
    initial.append(0)
program = list("A,B,A,C,A,B,C,C,A,B")
A = list("R,8,L,10,R,8")
B = list("R,12,R,8,L,8,L,12")
C = list("L,12,L,10,L,8")
programASCII = [ord(x) for x in program]
programASCII.append(10)
AASCII = [ord(x) for x in A]
AASCII.append(10)
BASCII = [ord(x) for x in B]
BASCII.append(10)
CASCII = [ord(x) for x in C]
CASCII.append(10)
# print(programASCII)
# print(AASCII)
# print(BASCII)
# print(CASCII)
fullCode = programASCII + AASCII + BASCII + CASCII
fullCode.append(ord('n'))
fullCode.append(10)
# print(fullCode)
programList[0] = fullCode[0]
while(True):
    runCode(initial)
    # print(chr(programList[1]))
    if(programList[3] == 3):
        break
print("here")
for x in fullCode[1:]:
    programList[0] = x
    runCode(initial)
while(True):
    runCode(initial)
    if(programList[3] == 99):
        break
print(programList[1])
