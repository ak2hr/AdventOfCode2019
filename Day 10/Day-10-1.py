import copy

counter = 0

def isBetween(out1, out2, in3):
    slope = 0
    slope2 = 0
    if(out1[0] == out2[0]):
        slope = "up"
    else:
        slope = abs((out1[1] - out2[1])/(out1[0] - out2[0]))
    if(in3[0] == out2[0]):
        slope2 = "up"
    else:
        slope2 = abs((in3[1] - out2[1])/(in3[0] - out2[0]))
    if(slope2 == slope):
        if((in3[0] >= out1[0] and in3[0] <= out2[0]) or (in3[0] <= out1[0] and in3[0] >= out2[0])):
            if((in3[1] >= out1[1] and in3[1] <= out2[1]) or (in3[1] <= out1[1] and in3[1] >= out2[1])):
                return True
    return False

def canSee(asteroid1, asteroid2, roidList):
    ret = 0
    tempList1 = copy.deepcopy(list(roidList))
    tempList1.remove(asteroid2)
    blocked = False
    for x in tempList1:
        if(isBetween(asteroid1, asteroid2, x)):
            blocked = True
    if(blocked):
            return False
    return True



#Station = (22,28)

file = open("C:/Users/akepley/Desktop/input.txt", "r")
lines = file.readlines()
curX = 0
curY = 0
asteroids = []
point = (22,28)
for line in lines:
    for y in line: 
        if(y == "#"):
            asteroids.append((curX,curY))
        curX += 1
    curX = 0
    curY += 1
fullDict = {}
quad1 = {}
quad2 = {}
quad3 = {}
quad4 = {}
asteroids.remove(point)
for asteroid in asteroids:
    slope = 0
    if(asteroid[0] >= point[0] and asteroid[1] < point[1]):
        if(asteroid[0] == point[0]):
            quad1[asteroid] = -1000
        else:
            quad1[asteroid] = (point[1] - asteroid[1])/(point[0] - asteroid[0])
    elif(asteroid[0] > point[0] and asteroid[1] >= point[1]):
        quad2[asteroid] = (point[1] - asteroid[1])/(point[0] - asteroid[0])
    elif(asteroid[0] <= point[0] and asteroid[1] > point[1]):
        if(asteroid[0] == point[0]):
            quad3[asteroid] = 1000
        else:
            quad3[asteroid] = (point[1] - asteroid[1])/(point[0] - asteroid[0])
    elif(asteroid[0] < point[0] and asteroid[1] <= point[1]):
        quad4[asteroid] = (point[1] - asteroid[1])/(point[0] - asteroid[0])
fullDict.update(sorted(quad1.items(), key=lambda item: item[1]))
fullDict.update(sorted(quad2.items(), key=lambda item: item[1]))
fullDict.update(sorted(quad3.items(), key=lambda item: item[1]))
fullDict.update(sorted(quad4.items(), key=lambda item: item[1]))
length = len(fullDict)
while(counter < length):
    removeList = []
    for key in fullDict.keys():
        if(canSee(point, key, fullDict.keys())):
            counter += 1
            print(counter, ": ", key)
            removeList.append(key)
    for x in removeList:
        fullDict.pop(x)
