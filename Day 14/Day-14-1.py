needed = {}
products = []
results = []

def addToNeeded(productList):
    for x in range(len(productList)):
        if(x % 2 == 1 and productList[x] in needed):
            needed[productList[x]] += productList[x-1]
        elif(x % 2 == 1 and productList[x] not in needed):
            needed[productList[x]] = productList[x-1]

file = open("Day 14/test3.txt", "r")
lines = file.readlines()
needed = {}
products = []
results = []
for line in lines:
    divide = line.rstrip().replace(",", "").split(" => ")
    products.append(divide[0].split(" "))
    results.append(divide[1].split(" "))
count = len(results)
for x in range(count):
    if("FUEL" in results[x]):
        addToNeeded(products[x])
print(needed)