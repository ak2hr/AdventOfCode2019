
poses = [
    [0,0,0],[0,0,0],[0,0,0],[0,0,0]
]

velocities = [
    [0,0,0],[0,0,0],[0,0,0],[0,0,0]
]


def getNewVelocity(moon):
    for x in range(4):
        if(x != moon):
            for y in range(3):
                if(poses[x][y] > poses[moon][y]):
                    velocities[moon][y] += 1
                elif(poses[x][y] < poses[moon][y]):
                    velocities[moon][y] -= 1



def getNewPosition(moon):
    for x in range(3):
        poses[moon][x] += velocities[moon][x]

file = open("C:/Users/akepley/Documents/AdventOfCode2019/Day 12/test2.txt", "r")
lines = file.readlines()


for x in range(4):
    tempLine = lines[x].rstrip().replace("<", "").replace(">","").split(",")
    for y in range(3):
        poses[x][y] = int(tempLine[y][tempLine[y].find("=") + 1:])

steps = 0
mySet = {0}
mySet.remove(0)
#while(True):
for x in range(1000000):
    for a in range(4):
        getNewVelocity(a)
    for a in range(4):
        getNewPosition(a)
    if(str(poses + velocities) in mySet):
        break
    else:
        mySet.add(str(poses+velocities))
    steps += 1
print(steps)
