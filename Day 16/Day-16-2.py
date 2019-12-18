import copy, math, pdb

file = open("Day 16/input.txt", "r")
contents = file.read()
contents = contents * 10000
numList =  list(map(int,list(contents)))
firstSeven = int(''.join(map(str, numList[:7])))
size = len(numList)
for q in range(100):
    for x in range(size - 2, firstSeven - 1, -1):
        numList[x] = (numList[x+1] + numList[x]) % 10
    print(q)
print(numList[firstSeven:firstSeven+8])
        