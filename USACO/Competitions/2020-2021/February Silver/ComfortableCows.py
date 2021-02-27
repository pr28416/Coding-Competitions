N = int(input())
coordDict = {}
coordList = []
scores = [0] * N
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
threes = set()

for i in range(N):
    newCoord = tuple(map(int, input().split(" ")))
    coordList.append(newCoord)
    coordDict[newCoord] = i

    for d in directions:
        key = (newCoord[0]+d[0], newCoord[1]+d[1])
        if key in coordDict:
            scores[i] += 1
            scores[coordDict[key]] += 1

    if scores[i] == 3:
        threes.add(newCoord)
    
    for d in directions:
        key = (newCoord[0]+d[0], newCoord[1]+d[1])
        if key in coordDict:

    
    print(scores)

