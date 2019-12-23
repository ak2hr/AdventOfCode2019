import copy

def newStack(pos):
    global size
    return size - 1 - pos

def cut(pos, num):
    global size
    if(num > 0):
        return (pos + num) % 10
    else:
        return (size + num + pos) % 10

def increment(pos, num):
    global size
    return ((size * num) - (pos * num)) % size

file = open("Day 22/input.txt", "r")
lines = file.readlines()
instructions = []
for x in lines:
    instructions.append(x.rstrip())

size = 10
repetitions = 101741582076661

# pos = 3
# print(pos)
# instructions.reverse()
# for x in instructions:
#     if(x[0] == 'd'):
#         if(x[5] == 'w'):  
#             pos = increment(pos, int(x[20:]))
#         else:
#             pos = newStack(pos)
#     else:
#         pos = cut(pos, int(x[4:]))
#     print(x, ": ", pos)

for x in range(10):
    print(increment(x, 9), end=' ')