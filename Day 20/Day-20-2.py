import copy

portalConnections = {}
portalSet = {0}
portalSet.remove(0)
discovered = {}
ret = {}

def addPointToPortalDict(x,y,portal):
    global portalDict
    if(portal != "AA"):
        portalSet.add(portal)
    if(portal not in portalDict):
        portalDict[portal] = [(x,y)]
    else:
        portalDict[portal].append((x,y))

def isPortal(point):
    global portalDict
    for x in portalDict:
        if(x != "AA"):
            for y in portalDict[x]:
                if(y == point):
                    for z in portalDict[x]:
                        if(z != point):
                            return([True, x, z])
                        elif(x == "ZZ"):
                            return([True, x, z])
    return([False, "AA", (0,0)])


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
                ret[portalResult[1]] = [steps, portalResult[2]]
            else:
                findAllPortals((x,y+1),steps+1)
                findAllPortals((x,y-1),steps+1)
                findAllPortals((x+1,y),steps+1)
                findAllPortals((x-1,y),steps+1)


def navigateMaze(point, steps):
    print(point, steps)
    global portalSet
    global ret
    ret.clear()
    discovered.clear()
    findAllPortals(point, 0)
    choices = copy.deepcopy(ret)
    portals = copy.deepcopy(portalSet)
    minimum = 10000
    for x in choices:
        if(x == "ZZ"):
            print(steps, ret)
            if(ret[x][0] < minimum):
                minimum = steps + ret[x][0]
        elif(x in portalSet):
            portalSet.remove(x)
            val = navigateMaze(ret[x][1], steps + ret[x][0] + 1)
            if(val < minimum):
                minimum = copy.deepcopy(val)
            ret = copy.deepcopy(choices)
            portalSet = copy.deepcopy(portals)
    return minimum
            
        



file = open("Day 20/input.txt", 'r')
lines = file.readlines()
height = len(lines)
width = len(lines[0].rstrip('\n'))

#create maze
maze = []
for line in lines:
    maze.append(line)
portalDict = {}

#add horizonal portals
for y in range(height):
    last = ''
    for x in range(width):
        if(maze[y][x] == '.' and 65 <= ord(last) <= 90):
            addPointToPortalDict(x,y,maze[y][x-2] + maze[y][x-1])
        elif(last == '.' and 65 <= ord(maze[y][x]) <= 90):
            addPointToPortalDict(x-1,y,maze[y][x] + maze[y][x+1])
        last = maze[y][x]       

#add vertical portals
for x in range(width):
    last = ''
    for y in range(height):
        if(maze[y][x] == '.' and 65 <= ord(last) <= 90):
            addPointToPortalDict(x,y,maze[y-2][x] + maze[y-1][x])
        elif(last == '.' and 65 <= ord(maze[y][x]) <= 90):
            addPointToPortalDict(x,y-1,maze[y][x] + maze[y+1][x])
        last = maze[y][x]

start = portalDict["AA"][0]
end = portalDict["ZZ"][0]

print(navigateMaze(start, 0))