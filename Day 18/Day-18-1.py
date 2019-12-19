import copy

discovered = {}
start = (0,0)
minimums = {}
ret = {}

def findAllKeys(curMap, curPos, steps):
    global ret
    x =  curPos[1]
    y = curPos[0]
    # if(curPos in discovered):
    #     if(steps < discovered[curPos]):
    #         discovered[curPos] = steps
    # else:
    #     discovered[curPos] = steps
    if(curMap[y][x] != '#' and (ord(curMap[y][x]) < 65 or ord(curMap[y][x]) > 90)):
        if(97 <= ord(curMap[y][x]) <= 122):
            if(curMap[y][x] in ret):
                if(steps < ret[curMap[y][x]]):
                    ret[curMap[y][x]] = steps
            else:
                ret[curMap[y][x]] = steps
        else:
            steps += 1
            if((y+1, x) not in discovered or discovered[(y+1,x)] > steps):
                discovered[(y+1,x)] = steps
                findAllKeys(curMap, (y+1, x), steps)
            if((y-1, x) not in discovered or discovered[(y-1,x)] > steps):
                discovered[(y-1,x)] = steps
                findAllKeys(curMap, (y-1, x), steps)
            if((y, x+1) not in discovered or discovered[(y,x+1)] > steps):
                discovered[(y,x+1)] = steps
                findAllKeys(curMap, (y, x+1), steps)
            if((y, x-1) not in discovered or discovered[(y,x-1)] > steps):
                discovered[(y,x-1)] = steps
                findAllKeys(curMap, (y, x-1), steps)


def collectKey(key, thisMap):
    door = key.upper()
    newPos = start
    for y in range(len(thisMap)):
        for x in range(len(thisMap[y])):
            if(thisMap[y][x] == key):
                thisMap[y][x] = '.'
                newPos = (y,x)
            if(thisMap[y][x] == door):
                thisMap[y][x] = '.'
    return (thisMap, newPos)



def getMinimumSteps(remove, curMap, curPos, recurse):
    global minimums
    global ret
    recurse += 1
    keyResult = collectKey(remove, curMap)
    curMap = keyResult[0]
    curPos = keyResult[1] 
    discovered.clear()
    ret = {}
    findAllKeys(curMap, curPos, 0)
    keys = copy.deepcopy(ret)
    if(recurse < 20):
        print(recurse, remove, keys)
    if(str(curPos)+str(keys) not in minimums):
        minimum = 100000
        if(len(keys) > 0):
            for x in copy.deepcopy(keys):
                val = keys[x] + getMinimumSteps(x, copy.deepcopy(curMap), copy.deepcopy(curPos), recurse)
                if(val < minimum):
                    minimum = val
            minimums[str(curPos)+str(keys)] = minimum
        else:
            minimums[str(curPos)+str(keys)] = 0
    return minimums[str(curPos)+str(keys)]



file = open("Day 18/input.txt", 'r')
lines = file.readlines()
origMap = []
for x in lines:
    temp = []
    for y in x.rstrip():
        temp.append(y)
    origMap.append(temp)
width = len(origMap[0])
height = len(origMap)
for y in range(height):
    for x in range(width):
        if(origMap[y][x] == '@'):
            start = (y,x)
print(getMinimumSteps('', copy.deepcopy(origMap), start, 0))