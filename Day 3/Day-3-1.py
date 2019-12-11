file = open("C:/Users/akepley/Desktop/input.txt", "r")
lines = file.readlines()
wire1 = lines[0].split(",")
wire2 = lines[1].split(",")
points1 = []
points2 = []
steps1 = []
steps2 = []
curx = 0
cury = 0
steps = 0
for vector in wire1:
    direction = vector[0]
    magnitude = int(vector[1:])
    if(direction == "U"):
        for x in range(magnitude):
            cury += 1
            points1.append((curx,cury))
            steps += 1
            steps1.append(steps)
    if(direction == "L"):
        for x in range(magnitude):
            curx -= 1
            points1.append((curx,cury))
            steps += 1
            steps1.append(steps)
    if(direction == "R"):
        for x in range(magnitude):
            curx += 1
            points1.append((curx,cury))
            steps += 1
            steps1.append(steps)
    if(direction == "D"):
        for x in range(magnitude):
            cury -= 1
            points1.append((curx,cury))
            steps += 1
            steps1.append(steps)
curx = 0
cury = 0
steps = 0
for vector in wire2:
    direction = vector[0]
    magnitude = int(vector[1:])
    if(direction == "U"):
        for x in range(magnitude):
            cury += 1
            points2.append((curx,cury))
            steps += 1
            steps2.append(steps)
    if(direction == "L"):
        for x in range(magnitude):
            curx -= 1
            points2.append((curx,cury))
            steps += 1
            steps2.append(steps)
    if(direction == "R"):
        for x in range(magnitude):
            curx += 1
            points2.append((curx,cury))
            steps += 1
            steps2.append(steps)
    if(direction == "D"):
        for x in range(magnitude):
            cury -= 1
            points2.append((curx,cury))
            steps += 1
            steps2.append(steps)
for x in range(len(points1)):
    for y in range(len(points2)):
        if(points1[x] == points2[y]):
            print(steps1[x] + steps2[y])