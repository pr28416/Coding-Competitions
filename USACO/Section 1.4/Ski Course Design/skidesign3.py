"""
ID: pranav.19
LANG: PYTHON3
TASK: skidesign
"""

N = 0
oldHills = []

with open("skidesign2.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        oldHills.append(int(f.readline()))

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
        n.append(a.pop(0))
    while len(b) > 0:
        n.append(b.pop(0))
        
    return n

def getPrice(n):
    t = 0
    for i in range(N):
        t += (n[i]-oldHills[i])**2
    return t
    

oldHills = split(oldHills)
newHills = oldHills.copy()
print(oldHills)
totalCost = 0

# START CODE

while max(newHills)-min(newHills) > 17:

    # Get index of largest and smallest
    x = newHills.index(max(newHills))
    y = newHills.index(min(newHills))

    # Find average
    avg = int((x+y)/2)

    # Add avg to smallest, subtract from smallest
    newHills[x] -= avg
    newHills[y] += avg

    # Get total amount to change by, set equal to change
    change = 17 - (newHills[x]-newHills[y])

    # Get change increments

    # CASE 1

    tester = newHills.copy()

    changeY1 = int(change/2)
    changeX1 = change - changeY1

    # Subtract smallest by first increment, increase largest by second increment
    tester[x] += changeX1
    tester[y] -= changeY1

    p1 = getPrice(tester)

    # CASE 2
    tester = newHills.copy()

    changeX2 = int(change/2)
    changeY2 = change - changeX2

    # Subtract smallest by first increment, increase largest by second increment
    tester[x] += changeX2
    tester[y] -= changeY2

    p2 = getPrice(tester)

    if p1 < p2:
        newHills[x] += changeX1
        newHills[y] -= changeY1
    else:
        newHills[x] += changeX2
        newHills[y] -= changeY2


    print(newHills) #"Modified to %s" % 


# print("Original: %s" % originalHills)
print("\nNew: %s" % newHills)
print("Max: %s, Min: %s" % (max(newHills), min(newHills)))

# Get final costs

for i in range(N):
    print((newHills[i]-oldHills[i])**2, end=" + ")
    totalCost += (newHills[i]-oldHills[i])**2

print()
print(totalCost)
with open("skidesign.out", "w") as f:
    f.write("{}\n".format(totalCost))