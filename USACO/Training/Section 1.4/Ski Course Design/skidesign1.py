"""
ID: pranav.19
LANG: PYTHON3
TASK: skidesign
"""

N = 0
originalHills = []

with open("skidesign.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        originalHills.append(int(f.readline()))

# print(N, originalHills)

def split(n):
    if len(n) == 1:
        return n
    else:
        a = split(n[:int(len(n)/2)])
        b = split(n[int(len(n)/2):])
        return merge(a, b)

def merge(a, b):
    n = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            n.append(a.pop(0))
        else:
            n.append(b.pop(0))
    while len(a) > 0:
        n.append(a.pop(0));
    while len(b) > 0:
        n.append(b.pop(0))
        
    return n

originalHills = split(originalHills)
newHills = originalHills.copy()
# print(originalHills)
totalCost = 0

myMaxIndex = 0
myMinIndex = 0

# print("Starting")
# print(originalHills)

while max(newHills)-min(newHills) > 17:
    # Get the index of the max and min
    myMaxIndex = newHills.index(max(newHills))
    myMinIndex = newHills.index(min(newHills))

    # Get halfway, and change each of them by half of that.
    incrementer = int((newHills[myMaxIndex]-newHills[myMinIndex])/2)+1
    newHills[myMinIndex] += incrementer
    newHills[myMaxIndex] -= incrementer
    # print(newHills)
    # Check if the distance between them is too little
    if newHills[myMaxIndex]-newHills[myMinIndex] < 17:
        # Check if the max >= min or else min > max 
        newHills[myMinIndex] -= 8
        newHills[myMaxIndex] += 9
        # print(newHills)

# print("Finished")

# print("Checking")
# print("myMinIndex[%s]: %s, myMaxIndex[%s]: %s)" % (myMinIndex, newHills[myMinIndex], myMaxIndex, newHills[myMaxIndex]))

for i in range(0, newHills.index(min(newHills))):
    newHills[i] = min(newHills)

for i in range(N-1, newHills.index(max(newHills)), -1):
    newHills[i] = max(newHills)

# print("Finished")

# Get final costs
for i in range(N):
    totalCost += (newHills[i]-originalHills[i])**2

# print(originalHills)
# print(newHills)
with open("skidesign.out", "w") as f:
    f.write("{}\n".format(totalCost))