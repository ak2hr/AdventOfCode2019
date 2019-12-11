from collections import Counter

def determine(number):
    increasing = True
    doubles = False
    noMore = False
    digits = [int(d) for d in str(number)]
    for y in range(len(digits) - 1):
        if(digits[y] > digits[y+1]):
            increasing  = False
        if(digits[y] == digits[y+1]):
            doubles = True
        counts = Counter(digits).values()
        for z in counts:
            if(z == 2):
                noMore = True
    if(increasing and doubles and noMore):
        return True
    else:
        return False

print(determine(112233))
print(determine(223450))
print(determine(123789))
print(determine(123444))
print(determine(111122))
count = 0
for x in range(134564, 585160):
    if(determine(x)):
        count += 1
print(count)