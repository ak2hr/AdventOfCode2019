def findOrbits(name, orbits):
    for x in orbits:
        if(x[0] == name):
            if(x[1] == "COM"):
                return 1
            else:
                return findOrbits(x[1], orbits) + 1

def makeOrbitList(name, orbits):
    ret = []
    for x in orbits:
        if(x[0] == name):
            ret.append(x[1])
            if(x[1] == "COM"):
                return ret
            else:
                ret = makeOrbitList(x[1], orbits)
                ret.append(x[1])
                return ret

def findFirstCommon(list1, list2):
    for x in list1:
        for y in list2:
            if(x == y):
                return x


file = open("C:/Users/akepley/Desktop/input.txt", "r")
lines = file.readlines()
newDict = {}
orbits = []
for line in lines:
    line = line.rstrip()
    orbits.append((line[line.find(")") + 1:len(line)], line[:line.find(")")]))
for orbit in orbits:
    if(orbit[0] not in newDict):
        newDict[orbit[0]] = 0
for key in newDict.keys():
    newDict[key] = makeOrbitList(key, orbits)
youList = newDict["YOU"][::-1]
sanList = newDict["SAN"][::-1]
common = findFirstCommon(youList, sanList)
print(youList.index(common) + sanList.index(common))