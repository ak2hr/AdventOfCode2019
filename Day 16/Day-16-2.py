import copy, math

file = open("Day 16/test4.txt", "r")
contents = file.read()
contents = contents * 10000
numList =  list(contents)
pattern = [0,1,0,-1]
nextPhase = copy.deepcopy(numList)
size = len(numList)
for q in range(100):
    for x in range(1, size + 1):
        
        nextPhase[x-1] = abs(total) % 10
    numList = copy.deepcopy(nextPhase)
    print(q)
print(numList)
        