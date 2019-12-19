import copy

discovered = {}

def findAllKeys(curMap, curPos, steps):
    ret = {0}
    ret.remove(0)
    x =  curPos[1]
    y = curPos[0]
    # print((x,y), curMap[y][x], ord(curMap[y][x]))
    discovered[curPos] = 0
    if(curMap[y][x] != '#' and (ord(curMap[y][x]) < 65 or ord(curMap[y][x]) > 90)):
        if(97 <= ord(curMap[y][x]) <= 122):
            ret.add((curMap[y][x]))
        else:
            steps += 1
            if((y+1, x) not in discovered):
                ret = ret|findAllKeys(curMap, (y+1, x), steps)
            if((y-1, x) not in discovered):
                ret = ret|findAllKeys(curMap, (y-1, x), steps)
            if((y, x+1) not in discovered):
                ret = ret|findAllKeys(curMap, (y, x+1), steps)
            if((y, x-1) not in discovered):
                ret = ret|findAllKeys(curMap, (y, x-1), steps)
    return ret


def collectKey(key, thisMap):
    door = key.upper()
    for y in thisMap:
        for x in thisMap:
            if(thisMap[y][x] == key or thisMap[y][x] == door):
                thisMap[y][x] = '.'
    return (thisMap, (y,x))



def getMinimumSteps(remove, curMap, curPos):
    curMap = collectKey(remove, curMap)[0] 
    discovered.clear()
    keys = findAllKeys(curMap, curPos, 0)
    if(len(keys) == 0):
        return 0
    else:
        minimum = 10000
        for x in keys:
            val = getMinimumSteps(x, curMap, curPos)
            if(val < minimum):
                minimum = val
    return val



file = open("Day 18/test5.txt", 'r')
lines = file.readlines()
origMap = []
for x in lines:
    temp = []
    for y in x.rstrip():
        temp.append(y)
    origMap.append(temp)
width = len(origMap[0])
height = len(origMap)
start = (0,0)
for y in range(height):
    for x in range(width):
        if(origMap[y][x] == '@'):
            start = (y,x)
getMinimumSteps('', origMap, start)