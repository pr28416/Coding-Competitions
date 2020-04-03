N = 0
coords = []
with open("triangles.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        coords.append([int(i) for i in f.readline().split(" ")])

# print(N)
# print(coords)

def findArea(a, b, c): # O(nlogn)
    sides = [((b[1]-a[1])**2+(b[0]-a[0])**2)**0.5, ((b[1]-c[1])**2+(b[0]-c[0])**2)**0.5, ((c[1]-a[1])**2+(c[0]-a[0])**2)**0.5]
    sides.sort()
    return (sides[0])*(sides[1])/2

def newFindArea(a, b, c): # b is the right-angle point, a is the y-axis point, c is the x-axis point
    # s1 = ((b[1]-c[1])**2+(b[0]-c[0])**2)**0.5
    dx = abs(c[0]-b[0])
    dy = abs(a[1]-b[1])
    return dx*dy

# print(findArea(coords[0], coords[2], coords[3]))

def getPointsOnXAxis(pointIdx): # O(n)
    return [i for i in range(pointIdx+1, len(coords)) if coords[i][1] == coords[pointIdx][1]]
    # possibleCoords = []
    # for i in range(pointIdx+1, len(coords)):
    #     if coords[i][1] == coords[pointIdx][1]:
    #         possibleCoords.append(i)
    # return possibleCoords

def getPointsOnYAxis(pointIdx): # O(n)
    return [i for i in range(pointIdx+1, len(coords)) if coords[i][0] == coords[pointIdx][0]]
    # possibleCoords = []
    # for i in range(pointIdx+1, len(coords)):
    #     if coords[i][0] == coords[pointIdx][0]:
    #         possibleCoords.append(i)
    # return possibleCoords

totalPossibleAreas = []

def split(x):
    if len(x) == 1:
        return x
    a = split(x[:len(x)//2])
    b = split(x[len(x)//2:])
    return merge(a, b)

def merge(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][0] < b[0][0]:
            x.append(a.pop(0))
        elif a[0][0] == b[0][0]:
            if a[0][1] < b[0][1]:
                x.append(a.pop(0))
            else:
                x.append(b.pop(0))
        else:
            x.append(b.pop(0))

    while len(a) > 0:
        x.append(a.pop(0))

    while len(b) > 0:
        x.append(b.pop(0))

    return x

# coords = split(coords)
# print(coords)

# Get a point
for pointIdx in range(len(coords)): # O(n)
    # Get a point on same x-axis
    xPoints = getPointsOnXAxis(pointIdx) # O(n)
    for xPoint in xPoints:# O(n)
        # Get a point on same y-axis
        yPoints = getPointsOnYAxis(pointIdx) + getPointsOnYAxis(xPoint)# O(n)
        for yPoint in yPoints: # O(n)
            print("X Using points: %s, %s, %s" % (coords[pointIdx], coords[xPoint], coords[yPoint]))
            totalPossibleAreas.append(newFindArea(coords[yPoint], coords[pointIdx], coords[xPoint]))
    
    yPoints = getPointsOnYAxis(pointIdx)
    for yPoint in yPoints:
        xPoints = getPointsOnXAxis(yPoint)
        for xPoint in xPoints:
            print("Y Using points: %s, %s, %s" % (coords[pointIdx], coords[xPoint], coords[yPoint]))
            totalPossibleAreas.append(findArea(coords[yPoint], coords[pointIdx], coords[xPoint]))

s = (int(sum(totalPossibleAreas))) % (10**9+7)

# print(totalPossibleAreas)
# print(s)

with open("triangles.out", "w") as f:
    f.write("%d\n" % s)