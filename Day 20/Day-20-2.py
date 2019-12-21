import copy

outerPortals = {}
innerPortals = {}
discovered = {}
ret = {}
currentIter = []
nextIter = []

def isPortal(point):
    if(point != outerPortals["AA"]):
        for x in outerPortals:
            if(point == outerPortals[x]):
                return [True, x, -1]
        for x in innerPortals:
            if(point == innerPortals[x]):
                return [True, x, 1]
    return [False, "AA", 0]

def findAllPortals(point, steps):
    global ret
    global maze
    global discovered
    x = point[0]
    y = point[1]
    if(maze[y][x] == '.'):
        if(point not in discovered):
            discovered[point] = steps
            portalResult = isPortal(point)
            if(portalResult[0] and steps > 0):
                ret[portalResult[1]] = [steps, point, portalResult[2]]
            else:
                findAllPortals((x,y+1),steps+1)
                findAllPortals((x,y-1),steps+1)
                findAllPortals((x+1,y),steps+1)
                findAllPortals((x-1,y),steps+1)

            
        
file = open("Day 20/input.txt", 'r')
lines = file.readlines()
height = len(lines)
width = len(lines[0].rstrip('\n'))

#create maze
maze = []
for line in lines:
    maze.append(line)

#add horizonal portals
for y in range(height):
    last = ''
    for x in range(width):
        if(maze[y][x] == '.' and 65 <= ord(last) <= 90):
            if(x == 2):
                outerPortals[maze[y][x-2] + maze[y][x-1]] = (x,y)
            else:
                innerPortals[maze[y][x-2] + maze[y][x-1]] = (x,y)
        elif(last == '.' and 65 <= ord(maze[y][x]) <= 90):
            if(x == width - 2):
                outerPortals[maze[y][x] + maze[y][x+1]] = (x-1,y)
            else:
                innerPortals[maze[y][x] + maze[y][x+1]] = (x-1,y)
        last = maze[y][x]       

#add vertical portals
for x in range(width):
    last = ''
    for y in range(height):
        if(maze[y][x] == '.' and 65 <= ord(last) <= 90):
            if(y == 2):
                outerPortals[maze[y-2][x] + maze[y-1][x]] = (x,y)
            else:
                innerPortals[maze[y-2][x] + maze[y-1][x]] = (x,y)
        elif(last == '.' and 65 <= ord(maze[y][x]) <= 90):
            if(y == height - 2):
                outerPortals[maze[y][x] + maze[y+1][x]] = (x,y-1)
            else:
                innerPortals[maze[y][x] + maze[y+1][x]] = (x,y-1)
        last = maze[y][x]  

#entry = [point, steps, level]
#ret[portalName] = [steps, point, upOrDown]

currentIter.append([outerPortals["AA"], 0, 0])
print(outerPortals)
print(innerPortals)
print(currentIter)
minimum = 100000

while(True):
    nextIter.clear()
    for x in currentIter:
        curPoint = x[0]
        curSteps = x[1]
        curLevel = x[2]
        ret.clear()
        discovered.clear()
        findAllPortals(curPoint, 0)
        for y in ret:
            retSteps = ret[y][0]
            retPoint = ret[y][1]
            retLevel = ret[y][2]
            if(y == "ZZ"):
                if(curLevel == 0):
                    if(curSteps + retSteps < minimum):
                        minimum = copy.deepcopy(curSteps + retSteps)
                        print(minimum)
            else:
                if(retLevel == 1):
                    nextIter.append([outerPortals[y], copy.deepcopy(curSteps + retSteps + 1), copy.deepcopy(curLevel + 1)])
                elif(curLevel > 0):
                    nextIter.append([innerPortals[y], copy.deepcopy(curSteps + retSteps + 1), copy.deepcopy(curLevel - 1)])
    currentIter = copy.deepcopy(nextIter)
    # print(currentIter)