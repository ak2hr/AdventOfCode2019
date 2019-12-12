
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

file = open("C:/Users/akepley/Documents/AdventOfCode2019/Day 12/input.txt", "r")
lines = file.readlines()


for x in range(4):
    tempLine = lines[x].rstrip().replace("<", "").replace(">","").split(",")
    for y in range(3):
        poses[x][y] = int(tempLine[y][tempLine[y].find("=") + 1:])

steps = 0
for x in range(1000):
    print("After ", steps, " steps:")
    for a in range(4):
        print("position: ", poses[a], ", ", "velocity: ", velocities[a])
    for a in range(4):
        getNewVelocity(a)
    for a in range(4):
        getNewPosition(a)
    steps += 1
total = 0
print("After ", steps, " steps:")
for a in range(4):
    print("position: ", poses[a], ", ", "velocity: ", velocities[a])
for x in range(4):
    potential = 0
    kinetic = 0
    for y in range(3):
        potential += abs(poses[x][y])
        kinetic += abs(velocities[x][y])
    total += (potential * kinetic)
print(total)