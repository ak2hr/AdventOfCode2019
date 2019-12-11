file = open("C:/Users/Andrew/Desktop/input.txt", "r")
lines = file.readlines()
sum = 0
for line in lines:
    val = int(line)
    print(val)
    newVal = int(val/3) - 2
    print(newVal)
    sum += newVal
print(sum)
