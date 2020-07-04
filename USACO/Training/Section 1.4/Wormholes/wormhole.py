"""
ID: pranav.19
LANG: PYTHON3
TASK: wormhole
"""
N = 0
coords = []

class Coord:
    x, y = 0, 0
    linkedCoord = None
    def __init__(self, x, y):
        self.x, self.y = x, y

    def printCoord(self):
        print("({}, {})".format(self.x, self.y))

    def printC(self):
        return "({}, {})".format(self.x, self.y)

    # def allCoord(self):
    #     print("({}, {}) to ({}, {})".format(self.x, self.y, self.tx, self.ty))

    def temp(self):
        return "({}, {}) to ({}, {})".format(self.x, self.y, self.linkedCoord.x, self.linkedCoord.y)

    def goRight(self):
        self.x += 1

    def equals(self, coord):
        return coord.x == self.x and coord.y == self.y

    def setLocation(self, coord):
        self.x, self.y = coord.x, coord.y

with open("wormhole.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        temp = f.readline().split(" ")
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        coords.append(Coord(temp[0], temp[1]))

# for a in range(N):
#     for b in range(a+1, N):
#         coordinateLinks[a].tx, coordinateLinks[a].ty = coordinateLinks[b].x, coordinateLinks[b].y
#         coordinateLinks[b].tx, coordinateLinks[b].ty = coordinateLinks[a].x, coordinateLinks[a].y
#         coordinateLinks[a].allCoord()
#         coordinateLinks[b].allCoord()
#         print("")

# for i in coordinateLinks:
    # i.allCoord()

answer = 0

# Creating all possible coordinate linkages
def createSituation(givenCoords, currentCoords, answer):
    if len(givenCoords) == 2:
        # print("remaining: {} and {}".format(givenCoords[0].printC(), givenCoords[1].printC()))
        coord1 = Coord(givenCoords[0].x, givenCoords[0].y)
        coord2 = Coord(givenCoords[1].x, givenCoords[1].y)
        coord1.linkedCoord, coord2.linkedCoord = coord2, coord1
        # coord1.linkedCoord = Coord(coord2.x, coord2.y)
        # coord2.linkedCoord = Coord(coord1.x, coord1.y)
        
        currentCoords.append(coord1)
        currentCoords.append(coord2)

        # Test all coordinates
        print("-----------")
        for c in currentCoords:
            print("{}, ".format(c.temp()))
        print("-----------")
        if testSituation(currentCoords):
            answer += 1

        currentCoords.clear()
        return answer
    else:
        a = 0
        # for a in range(len(givenCoords)):
        for b in range(1, len(givenCoords)):
            # Create new linked coordinates
            print("\n---------------------------\n")
            print("a: {}, b: {}".format(a, b))
            coord1 = Coord(givenCoords[a].x, givenCoords[a].y)
            coord2 = Coord(givenCoords[b].x, givenCoords[b].y)
            # coord1.linkedCoord = Coord(coord2.x, coord2.y)
            # coord2.linkedCoord = Coord(coord1.x, coord1.y)
            coord1.linkedCoord = Coord(coord2.x, coord2.y)
            coord2.linkedCoord = Coord(coord1.x, coord1.y)

            # Add these new coordinates to currentCoords
            currentCoords.append(coord1)
            currentCoords.append(coord2)

            newGiven = givenCoords.copy()

            # print("removing {} and {}".format(newGiven[a].printC(), newGiven[b].printC()))

            del newGiven[a]
            del newGiven[b-1]

            answer = createSituation(newGiven, currentCoords, answer)
                
            # break
    return answer

answer = 0
def testSituation(givenCoords): # Returns false for no loops, true for loops
    # Get largest x
    xMax = 0
    for c in givenCoords:
        if c.x > xMax:
            xMax = c.x
    # Start at a coord
    # print("starting")
    for coord in givenCoords:
        cow = Coord(coord.x, coord.y)
        print("Cow starts at: {}".format(cow.printC()))
        prevLocations = [Coord(cow.x, cow.y)]

        print("Currently visited locations: ", end="")
        for i in prevLocations:
            print(i.printC(), end=", ")
        print()
        
        while cow.x <= xMax:
            cow.goRight()
            print("Going right -> {}".format(cow.printC()))

            # print("Currently visited locations: ", end="")
            # for i in prevLocations:
            #     print(i.printC(), end=",^^& ")
            # print()

            # Check if location was visited previously
            for i in prevLocations:
                if cow.equals(i):
                    print("Found loop! Cow from {} already stepped on {}".format(cow.printC(), i.printC()))
                    return True # RETURN: There was a loop!
            else: # Location was not visited previously
                # Check if cow is on a wormhole
                prevLocations.append(Coord(cow.x, cow.y))

                # print("Currently visited locations: ", end="")
                # for i in prevLocations:
                #     print(i.printC(), end=", ")
                # print()

                for i in givenCoords:
                    if cow.equals(i):
                        print("Stepped on wormhole! Setting location from {} to {}".format(cow.printC(), i.linkedCoord.printC()))
                        cow.setLocation(i.linkedCoord)
                        break
        print("Cow reached max value! There is no infinite loop here.\n")
        prevLocations.clear()
    return False

            
            
        # Go to the coord's linked coord

answer = createSituation(coords, [], answer)
print(answer)
with open("wormhole.out", "w") as f:
    f.write("{}\n".format(answer))
