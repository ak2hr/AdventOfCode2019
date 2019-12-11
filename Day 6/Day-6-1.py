def findOrbits(name, orbits):
    for x in orbits:
        if(x[0] == name):
            if(x[1] == "COM"):
                return 1
            else:
                return findOrbits(x[1], orbits) + 1




file = open("C:/Users/akepley/Desktop/input.txt", "r")
lines = file.readlines()
nameSize = 1
newDict = {}
orbits = []
for line in lines:
    line = line.rstrip()
    orbits.append((line[line.find(")") + 1:len(line)], line[:line.find(")")]))
for orbit in orbits:
    if(orbit[0] not in newDict):
        newDict[orbit[0]] = 0
total = 0
for key in newDict.keys():
    val = findOrbits(key, orbits)
    total += val
print(total)