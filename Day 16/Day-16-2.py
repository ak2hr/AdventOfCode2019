import copy, math

file = open("Day 16/input.txt", "r")
contents = file.read()
contents = contents * 10000
numList =  list(contents)
pattern = [0,1,0,-1]
nextPhase = copy.deepcopy(numList)
size = len(numList)
for q in range(100):
    currentPat = 0
    for x in range(1, size + 1):
        total = 0
        currentPat = 0
        for y in range(1, size + 1):
            if(y % x == 0):
                currentPat += 1
            patternVal = pattern[currentPat % 4]
            addVal = int(numList[y-1]) * patternVal
            total += addVal
        nextPhase[x-1] = abs(total) % 10
    numList = copy.deepcopy(nextPhase)
    print(q)
print(numList)
        