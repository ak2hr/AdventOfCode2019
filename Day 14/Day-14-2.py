import copy, math

needed = {}
have = {}
inputs = []
outputs = []

def onlyOre():
    for x in needed:
        if(x != "ORE" and needed[x] > 0):
            return False
    return True

def addToNeeded(reactants):
    for y in reactants:
        if(y in needed):
            needed[y] += reactants[y]
        else:
            needed[y] = reactants[y]
        if(y in have):
            if(have[y] >= needed[y]):
                have[y] -= needed[y]
                needed[y] = 0
            else:
                needed[y] -= have[y]
                have[y] = 0

def make(reactants, product):
    for x in product:
        while(needed[x] > 0):
            needed[x] -= product[x]
            for y in reactants:
                if(y in needed):
                    needed[y] += reactants[y]
                else:
                    needed[y] = reactants[y]
                if(y in have):
                    if(have[y] >= needed[y]):
                        have[y] -= needed[y]
                        needed[y] = 0
                    else:
                        needed[y] -= have[y]
                        have[y] = 0


def findReactionAndMake(productList):
    for x in productList:
        reactants = {}
        product = {}
        for y in range(len(outputs)):
            if(x in outputs[y]):
                product = outputs[y]
                reactants = inputs[y]
                break
        make(reactants, product)

        

file = open("Day 14/input.txt", "r")
lines = file.readlines()
for line in lines:
    divide = line.rstrip().replace(",", "").split(" => ")
    divide[0] = divide[0].split(" ")
    divide[1] = divide[1].split(" ")
    temp1 = {}
    for x in range(len(divide[0])):
        if(x % 2 == 1):
            temp1[divide[0][x]] = int(divide[0][x-1])
    temp2 = {}
    for x in range(len(divide[1])):
        if(x % 2 == 1):
            temp2[divide[1][x]] = int(divide[1][x-1])
    inputs.append(temp1)
    outputs.append(temp2)
for x in inputs:
    for y in x:
      if(y != "ORE" and y not in have):
          have[y] = 0  
fuel = 0
OreSoFar = 0
zeroes = str(copy.deepcopy(have))
while(True):
    needed = {}
    count = len(outputs)
    for x in range(count):
        if("FUEL" in outputs[x]):
            addToNeeded(inputs[x])
    while(True):
        findReactionAndMake(copy.deepcopy(list(needed.keys())))
        if(onlyOre()):
            break
    for x in needed:
        if(needed[x] < 0):
            if(x in have):
                have[x] += abs(needed[x])
            else:
                have[x] = abs(needed[x])
    OreSoFar += needed["ORE"]
    if(OreSoFar > 1000000000000):
        break
    fuel += 1
    print(fuel, ", ", OreSoFar)
print(fuel)

# print(fuel, ", ", OreSoFar, ", ", have)
# loopFuel = math.floor(1000000000000/OreSoFar) * (fuel)
# oreLeft = 1000000000000 - ((math.floor(1000000000000/OreSoFar)) * OreSoFar)
# fuel = 0
# while(True):
#     needed = {}
#     count = len(outputs)
#     for x in range(count):
#         if("FUEL" in outputs[x]):
#             addToNeeded(inputs[x])
#     while(True):
#         findReactionAndMake(copy.deepcopy(list(needed.keys())))
#         if(onlyOre()):
#             break
#     for x in needed:
#         if(needed[x] < 0):
#             if(x in have):
#                 have[x] += abs(needed[x])
#             else:
#                 have[x] = abs(needed[x])
#     oreLeft -= needed["ORE"]
#     if(oreLeft < 0):
#         break
#     fuel += 1
# print(loopFuel + fuel)