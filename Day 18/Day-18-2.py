import copy

#curPos, steps, curKeys

robots = [
    [(0,0), 0, {}],
    [(0,0), 0, {}],
    [(0,0), 0, {}],
    [(0,0), 0, {}]
]

discovered = {}
minimums = {}
ret = {}

def findAllKeys(curMap, curPos, steps):
    global ret
    x =  curPos[1]
    y = curPos[0]
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
    newPos = (0,0)
    for y in range(len(thisMap)):
        for x in range(len(thisMap[y])):
            if(thisMap[y][x] == key):
                thisMap[y][x] = '.'
                newPos = (y,x)
            if(thisMap[y][x] == door):
                thisMap[y][x] = '.'
    return (thisMap, newPos)



def getMinimumSteps(curMap, recurse):
    global robots
    global minimums
    global ret
    recurse += 1
    keys = {}

    for x in robots:
        discovered.clear()
        ret.clear()
        findAllKeys(curMap, x[0], 0)
        x[2] = copy.deepcopy(ret)
        keys.update(copy.deepcopy(ret))
    

    keySave = copy.deepcopy(keys)
    robotSave = copy.deepcopy(robots)
    mapSave = copy.deepcopy(curMap)

    if(recurse < 23):
        print(recurse)

    if(str(robots) not in minimums):
        minimum = 10000
        if(len(keys) == 0):
            minimums[str(robots)] = robots[0][1] + robots[1][1] + robots[2][1] + robots[3][1]
        else:
            for x in keys:
                keyResult = collectKey(x, curMap)
                curMap = copy.deepcopy(keyResult[0])
                for y in robots:
                    for z in y[2]:
                        if(x in z):
                            y[0] = copy.deepcopy(keyResult[1])
                            y[1] += copy.deepcopy(keys[x])
                val = getMinimumSteps(curMap, recurse)
                if(val < minimum):
                    minimum = copy.deepcopy(val)
                    minimums[str(robotSave)] = copy.deepcopy(minimum)
                curMap = copy.deepcopy(mapSave)
                keys = copy.deepcopy(keySave)
                robots = copy.deepcopy(robotSave)
    return minimums[str(robots)]


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
robot = 0
for y in range(height):
    for x in range(width):
        if(origMap[y][x] == '@'):
            robots[robot][0] = (y,x)
            robot += 1
print(getMinimumSteps(copy.deepcopy(origMap), 0))
print(robots)