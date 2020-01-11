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
        self.x = x
        self.y = y

    def setLinkedCoord(self, coord):
        c = Coord(coord.x, coord.y)
        self.linkedCoord = c

    def goRight(self):
        self.x += 1

    def setLocation(self, coord):
        self.x, self.y = coord.x, coord.y

    def equals(self, coord):
        return coord.x == self.x and coord.y == self.y


with open("wormhole.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        temp = f.readline().split(" ")
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        coords.append(Coord(temp[0], temp[1]))

# Create pairings
def createSituation(remaining, current, answer):
    if len(remaining) == 0:
        if testSituation(current):
            answer += 1
        return answer
    else:
        # Create a link with the first coord in remaining and any other coord
        # print("remaining: {}".format(len(remaining)))
        for a in range(1, len(remaining)):

            # Select coordinate
            coord2 = remaining.pop(a)
            coord1 = remaining.pop(0)
            coord1.setLinkedCoord(coord2)
            coord2.setLinkedCoord(coord1)

            current.append(coord1)
            current.append(coord2)

            # Explore remaining options
            answer = createSituation(remaining, current, answer)

            # Deselect coordinate
            remaining.insert(0, coord1)
            remaining.insert(a, coord2)
            del current[len(current)-1]
            del current[len(current)-1]

            coord2.setLinkedCoord(Coord(0, 0))
        return answer

def getNextWormhole(cow, given):
    closest = Coord(1000000000000000000, 1000000000000000000)
    for w in given:
        if cow.y == w.y and cow.x < w.x and w.x < closest.x:
            closest = Coord(w.x, w.y)
            closest.linkedCoord = w.linkedCoord
    return closest

def testSituation(wormholes):
    # Get the max x value the cow can travel
    xMax = 0
    for i in wormholes:
        if i.x > xMax: xMax = i.x
    
    for i in wormholes:
        # Create a new cow
        cow = Coord(i.x, i.y)
        # Reset the previous visited locations
        prevLocations = []
        repeat = True
        while repeat:
            repeat = False
            # Move the cow to the next wormhole on the same axis
            sentWormhole = getNextWormhole(cow, wormholes)
            cow.setLocation(sentWormhole)
            
            if cow.x > xMax:
                break

            # Check if wormhole was visited previously
            for i in prevLocations:
                if cow.equals(i):
                    return True  # RETURN: There was a loop!
            else:  # Location was not visited previously
                prevLocations.append(Coord(cow.x, cow.y))
                cow.setLocation(sentWormhole.linkedCoord)
                repeat = True
                rCount += 1
    else:
        return False

answer = createSituation(coords, [], 0)
# print(answer)
with open("wormhole.out", "w") as f:
    f.write("{}\n".format(answer))
