"""
ID: pranav.19
LANG: PYTHON3
TASK: castle
"""

M, N = 0, 0
floorplan = []
with open("castle.in", "r") as f:
    temp = f.readline().split(" ")
    M, N = int(temp[0]), int(temp[1])
    for i in range(N):
        floorplan.append([int(i) for i in f.readline().split(" ")])

def printRooms():
    print("Rooms:")
    for i in floorplan:
        for j in i:
            # print(getIntersections(j[0]), end="\t\t")
            print(j[1], end="\t\t")
        print()

# Get direction(s) of space between two squares (N, E, S, W)
def getIntersections(x):
    remaining = ["s", "e", "n", "w"]
    for i in x:
        del remaining[remaining.index(i)]
    fin = ""
    for i in remaining:
        fin += i
    return fin

# print(M, N)

# Set up floor plan
for i in range(N):
    for j in range(M):
        a = [
            [1, "w"],
            [2, "n"],
            [4, "e"],
            [8, "s"]
        ]
        walls = ""
        while floorplan[i][j] > 0:
            popped = a.pop()
            if floorplan[i][j] >= popped[0]:
                walls += popped[1]
                floorplan[i][j] -= popped[0]
        floorplan[i][j] = [walls, 0] # locations of walls, available squares to extend into

# for i in floorplan:
#     for j in i:
#         print(j[0], end="\t\t")
#     print()

# print()

# printRooms()

# Get the next position to start looking at; row, col --> current square, id = marking id (ex: -2)
def getNextPosition(row, col, id, count):
    intersections = getIntersections(floorplan[row][col][0])
    # Mark current as id
    floorplan[row][col][1] = id
    for i in intersections:
        if i == "s":
            if floorplan[row+1][col][1] != floorplan[row][col][1]:
                getNextPosition(row+1, col, id, count + 1)
        elif i == "e":
            if floorplan[row][col+1][1] != floorplan[row][col][1]:
                getNextPosition(row, col+1, id, count + 1)
        elif i == "n":
            if floorplan[row-1][col][1] != floorplan[row][col][1]:
                getNextPosition(row-1, col, id, count + 1)
        elif i == "w":
            if floorplan[row][col-1][1] != floorplan[row][col][1]:
                getNextPosition(row, col-1, id, count + 1)
    # End of traversal

# print("New")
# getNextPosition(0, 0, -2, 1)

# GET ROOM SIZES
# Search entire floorplan and mark which rooms are which
cont = True
ids = [i for i in range(1, 2502)]
while cont:
    cont = False
    for i in range(N):
        for j in range(M):
            if floorplan[i][j][1] == 0:
                cont = True
                getNextPosition(i, j, ids.pop(0), 1)
                break
# printRooms()
# used --> Stores [id, size] where id --> room id, size --> room size

used = [[i, 0] for i in range(1, ids[0])]
for i in floorplan:
    for j in i:
        used[j[1]-1][1] += 1
roomSizes = [i[1] for i in used]
# print("Room Sizes:", *roomSizes)
# print("Largest Room Size:", max(roomSizes))

largestRoom = max(roomSizes)
positionAtBrokenRoom = []

def breakWall(row, col, direction):
    global largestRoom, positionAtBrokenRoom
    sum1 = used[floorplan[row][col][1] - 1][1]
    sum2 = 0
    # Break wall and combine values
    if direction == "s":
        sum2 = used[floorplan[row + 1][col][1] - 1][1]
    elif direction == "e":
        sum2 = used[floorplan[row][col + 1][1] - 1][1]
    elif direction == "n":
        sum2 = used[floorplan[row - 1][col][1] - 1][1]
    elif direction == "w":
        sum2 = used[floorplan[row][col - 1][1] - 1][1]
    combined = sum1 + sum2
    # Check if combined value should precede the current largestRoom value
    if combined > largestRoom:
        # print("Checking for regular max: %s > largestRoom (%s)" % (combined, largestRoom))
        largestRoom = combined
        positionAtBrokenRoom = [row, col, direction]
    elif combined >= largestRoom:
        if len(positionAtBrokenRoom) == 0:
            # print("Checking if list is empty: %s = largestRoom (%s)" % (combined, largestRoom))
            largestRoom = combined
            positionAtBrokenRoom = [row, col, direction]
        elif positionAtBrokenRoom[1] > col:
            # print("Checking for regular max: %s = largestRoom (%s)" % (combined, largestRoom))
            largestRoom = combined
            positionAtBrokenRoom = [row, col, direction]
        elif positionAtBrokenRoom[1] == col:
            if positionAtBrokenRoom[0] < row:
                largestRoom = combined
                positionAtBrokenRoom = [row, col, direction]
            elif positionAtBrokenRoom[0] == row:
                if direction == "n" and positionAtBrokenRoom[2] == "e":
                    largestRoom = combined
                    positionAtBrokenRoom = [row, col, direction]

# Create modified floor plan
modifiedFloorPlan = []
for i in floorplan:
    temp = []
    for j in i:
        temp.append(j[1])
    modifiedFloorPlan.append(temp)

# for i in modifiedFloorPlan:
#     for j in i:
#         print(j, end="\t")
#     print()

# Find and break walls
for row in range(N):
    for col in range(M):
        # Check all sides
        # East
        if col != M-1:
            if modifiedFloorPlan[row][col] != modifiedFloorPlan[row][col+1]:
                # print("Breaking at %s %s %s for ori: %s, ext: %s" % (row+1, col+1, "e", modifiedFloorPlan[row][col], modifiedFloorPlan[row][col+1]))
                breakWall(row, col, "e")
        # West
        if col != 0:
            if modifiedFloorPlan[row][col] != modifiedFloorPlan[row][col-1]:
                # print("Breaking at %s %s %s for ori: %s, ext: %s" % (row + 1, col + 1, "w", modifiedFloorPlan[row][col], modifiedFloorPlan[row][col-1]))
                breakWall(row, col, "w")
        # North
        if row != 0:
            if modifiedFloorPlan[row][col] != modifiedFloorPlan[row-1][col]:
                # print("Breaking at %s %s %s for ori: %s, ext: %s" % (row + 1, col + 1, "n", modifiedFloorPlan[row][col], modifiedFloorPlan[row-1][col]))
                breakWall(row, col, "n")
        # South
        if row != N-1:
            if modifiedFloorPlan[row][col] != modifiedFloorPlan[row+1][col]:
                # print("Breaking at %s %s %s for ori: %s, ext: %s" % (row + 1, col + 1, "s", modifiedFloorPlan[row][col], modifiedFloorPlan[row+1][col]))
                breakWall(row, col, "s")

positionAtBrokenRoom[0], positionAtBrokenRoom[1] = positionAtBrokenRoom[0]+1, positionAtBrokenRoom[1]+1
positionAtBrokenRoom[2] = positionAtBrokenRoom[2].upper()
# print(largestRoom, "\n", *positionAtBrokenRoom)
with open("castle.out", "w") as f:
    f.write("%s\n%s\n" % (len(roomSizes), max(roomSizes)))
    f.write("%s\n%s %s %s\n" % (largestRoom, positionAtBrokenRoom[0], positionAtBrokenRoom[1], positionAtBrokenRoom[2]))
