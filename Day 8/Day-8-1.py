def printPixels(pixels, height, width):
    for x in range(height):
        for y in range(width):
            print(pixels[x][y], end='')
        print()

file = open("C:/Users/Student/Desktop/input.txt","r")
input = file.read()
height = 6
width = 25
pixels = [[],[],[],[],[],[]]
for x in range(height):
    for y in range(width):
        pixels[x].append(2)
pixelIndex = 0
for z in range(int(len(input) / (width * height))):
    for x in range(height):
        for y in range(width):
            if(pixels[x][y] == 2 and input[pixelIndex] != "2"):
                pixels[x][y] = input[pixelIndex]
            pixelIndex += 1
printPixels(pixels, height, width)