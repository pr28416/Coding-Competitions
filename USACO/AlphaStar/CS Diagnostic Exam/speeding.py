N, M = map(int, input().split(" "))
roads = [list(map(int, input().split(" "))) for i in range(N)]
bessie = [list(map(int, input().split(" "))) for i in range(M)]

# print(N, M)
# print(roads)
# print(bessie)

prT = pbT = 0
for r in range(len(roads)):
    length = roads[r][0]
    roads[r] = [prT, prT + length, roads[r][1]]
    prT += length

for b in range(len(bessie)):
    length = bessie[b][0]
    bessie[b] = [pbT, pbT + length, bessie[b][1]]
    pbT += length

# print(roads)
# print(bessie)

# roads:    [[0, 40, 75], [40, 90, 35], [90, 100, 45]]
# bessie:   [[0, 40, 76], [40, 60, 30], [60, 100, 40]]

maxAmt = 0
b = 0
for r in range(len(roads)):
    for b in range(len(bessie)):
        if bessie[b][1] <= roads[r][0]: continue
        elif bessie[b][0] >= roads[r][1]: break

        if bessie[b][2] > roads[r][2] and bessie[b][2] - roads[r][2] > maxAmt:
            maxAmt = bessie[b][2] - roads[r][2]


    # while b < len(bessie) and (bessie[b][1] <= roads[r][1] or bessie[b][0] >= roads[r][0]):
    #     if bessie[b][2] > roads[r][2] and bessie[b][2] - roads[r][2] > maxAmt:
    #         maxAmt = bessie[b][2] - roads[r][2]
    #     b += 1

print(maxAmt)
