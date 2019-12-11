file = open("C:/Users/akepley/Desktop/input.txt", "r")
content = file.read()
numList = content.split(",")
for x in range(len(numList)):
    numList[x] = int(numList[x])
curCode = 0
while(True):
    if(numList[curCode] == 99):
        print(numList[0])
        break
    if(numList[curCode] == 1):
        newVal = numList[numList[curCode + 1]] + numList[numList[curCode + 2]]
        numList[numList[curCode + 3]] = newVal
    if(numList[curCode] == 2):
        newVal = numList[numList[curCode + 1]] * numList[numList[curCode + 2]]
        numList[numList[curCode + 3]] = newVal
    curCode += 4