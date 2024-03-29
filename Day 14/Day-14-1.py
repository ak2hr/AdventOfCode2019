import copy

needed = {}
inputs = []
outputs = []

def onlyOre():
    for x in needed:
        if(x != "ORE" and needed[x] > 0):
            return False
    return True

def addToNeeded(productList):
    for x in productList:
        if(x in needed):
            needed[x] += productList[x]
        else:
            needed[x] = productList[x]

def make(reactants, product):
    for x in product:
        while(needed[x] > 0):
            needed[x] -= product[x]
            for y in reactants:
                if(y in needed):
                    needed[y] += reactants[y]
                else:
                    needed[y] = reactants[y]

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
count = len(outputs)
for x in range(count):
    if("FUEL" in outputs[x]):
        addToNeeded(inputs[x])
while(True):
    findReactionAndMake(copy.deepcopy(list(needed.keys())))
    if(onlyOre()):
        break
print(needed['ORE'])