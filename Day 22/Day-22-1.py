import copy

def newStack(thisDeck):
    thisDeck.reverse()

def cut(thisDeck, num):
    temp = thisDeck[num:] + thisDeck[:num]
    return temp

def increment(thisDeck, num):
    temp = copy.deepcopy(thisDeck)
    for x in range(0, len(thisDeck)*num, num):
        temp[x % len(thisDeck)] = thisDeck[int(x / num)]
    return temp



file = open("Day 22/input.txt", "r")
lines = file.readlines()
instructions = []
for x in lines:
    instructions.append(x.rstrip())

size = 10
deck = []
newDeck = []
for x in range(size):
    deck.append(x)

# for x in instructions:
#     if(x[0] == 'd'):
#         if(x[5] == 'w'):
#             newDeck = increment(deck, int(x[20:]))
#         else:
#             newStack(deck)
#             newDeck = copy.deepcopy(deck)
#     else:
#         newDeck = cut(deck, int(x[4:]))
#     deck = copy.deepcopy(newDeck)

# for x in range(size):
#     if(deck[x] == 2019):
#         print(x)

print(increment(deck, 9))