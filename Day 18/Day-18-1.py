file = open("Day 18/test1.txt", 'r')
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
            start = (x,y)
