bill1 = []
bill2 = []
truck = []
with open("billboard.in", "r") as f:
    bill1 = [int(i) for i in f.readline().split(" ")]
    bill2 = [int(i) for i in f.readline().split(" ")]
    truck = [int(i) for i in f.readline().split(" ")]


sx, lx = min(bill1[0], bill2[0], truck[0]), max(bill1[2], bill2[2], truck[2])
sy, ly = min(bill1[1], bill2[1], truck[1]), max(bill1[3], bill2[3], truck[3])
grid = [[0 for i in range(lx-sx)] for i in range(ly-sy)]
# [[0] * (lx-sx)] * (ly-sy)

# print("(%s, %s), (%s, %s)" % (sx, sy, lx, ly))

# print("adding billboard 1 - (%s, %s) to (%s, %s)" % (bill1[0]-sx, bill1[1]-sy, bill1[2]-sx, bill1[3]-sy))

for y in range(bill1[1]-sy, bill1[3]-sy):
    for x in range(bill1[0]-sx, bill1[2]-sx):
        grid[y][x] = 1

# for i in grid: print(i)
# print("adding billboard 2 - (%s, %s) to (%s, %s)" % (bill2[0]-sx, bill2[1]-sy, bill2[2]-sx, bill2[3]-sy))

for y in range(bill2[1]-sy, bill2[3]-sy):
    for x in range(bill2[0]-sx, bill2[2]-sx):
        grid[y][x] = 1

# for i in grid: print(i)
# print("adding truck - (%s, %s) to (%s, %s)" % (truck[0]-sx, truck[1]-sy, truck[2]-sx, truck[3]-sy))

for y in range(truck[1]-sy, truck[3]-sy):
    for x in range(truck[0]-sx, truck[2]-sx):
        grid[y][x] = 0

# for i in grid: print(i)
with open("billboard.out", "w") as f:
    c = 0
    for i in grid:
        for j in i:
            if j == 1:
                c += 1
    f.write("%s\n" % c)
