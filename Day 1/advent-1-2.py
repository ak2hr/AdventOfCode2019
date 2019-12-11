def allFuel(val):
    total = 0
    while(True):
        newVal = int(val/3) - 2
        if(newVal < 0):
            return total
        total += newVal
        val = newVal

file = open("C:/Users/Andrew/Desktop/input.txt", "r")
lines = file.readlines()
sum = 0
for line in lines:
    sum += allFuel(int(line))
print(sum)