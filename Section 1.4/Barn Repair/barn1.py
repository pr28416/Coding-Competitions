"""
ID: pranav.19
LANG: PYTHON3
TASK: barn1
"""
# M: Max number of boards that can be purchased
# S: Total number of stalls
# C: Total number of occupied stalls
M, S, C = 0, 0, 0
stallsWithCows = []
with open("barn1.in", "r") as f:
    line1 = f.readline().split(" ")
    M, S, C = int(line1[0]), int(line1[1]), int(line1[2])
    for i in range(C):
        stallsWithCows.append(int(f.readline()))

# Merge Sort
def split(x):
    if len(x) == 1:
        return x
    else:
        a = split(x[0:int(len(x)/2)])
        b = split(x[int(len(x)/2):])
        return merge(a, b)


def merge(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            x.append(a.pop(0))
        else:
            x.append(b.pop(0))
    while len(a) > 0:
        x.append(a.pop(0))
    while len(b) > 0:
        x.append(b.pop(0))
    return x
# --------
stallsWithCows = split(stallsWithCows)
ranges = []

totalLength = 0
if S == 1 and C == 1:
    totalLength = 1
elif S == 1 and C == 0:
    totalLength = 0
elif M >= C:
    totalLength = C
else:
    for i in stallsWithCows:
        ranges.append([i, i])

while len(ranges) > M:
    marker = 0
    currentLargest = 1000000000000
    for i in range(len(ranges)-1):
        if abs(ranges[i][1]-ranges[i+1][0]) < currentLargest:
            currentLargest = abs(ranges[i][1]-ranges[i+1][0])
            marker = i
    ranges[marker][1] = ranges[marker+1][1]
    del ranges[marker+1]

for e, i in enumerate(ranges):
    totalLength += i[1]-i[0]+1

with open("barn1.out", "w") as f:
    f.write("%s\n" % totalLength)
