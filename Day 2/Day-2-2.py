def runCode(numList):
    curCode = 0
    while(True):
        if(numList[curCode] == 99):
            return(numList[0])
        if(numList[curCode] == 1):
            newVal = numList[numList[curCode + 1]] + numList[numList[curCode + 2]]
            numList[numList[curCode + 3]] = newVal
        if(numList[curCode] == 2):
            newVal = numList[numList[curCode + 1]] * numList[numList[curCode + 2]]
            numList[numList[curCode + 3]] = newVal
        curCode += 4

file = open("C:/Users/akepley/Desktop/input.txt", "r")
content = file.read()
initial = content.split(",")
for x in range(len(initial)):
    initial[x] = int(initial[x])
for x in range(99):
    for y in range(99):
        temp = initial.copy()
        temp[1] = x
        temp[2] = y
        try:
            if(runCode(temp) == 19690720):
                print(temp)
        except:
            print("OOF")