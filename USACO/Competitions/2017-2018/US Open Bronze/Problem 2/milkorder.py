N, M, K = 0, 0, 0
hierarchy = None
order = None
with open("milkorder.in", "r") as f:
    N, M, K = [int(i) for i in f.readline().split(" ")]
    order = [0] * N
    hierarchy = tuple(int(i) for i in f.readline().split(" "))
    for i in range(K):
        temp = tuple(int(i) for i in f.readline().split(" "))
        order[temp[1]-1] = temp[0]

hierarchyPositions = [-1] * M

print("preorder:", order)

# Log pre-known hierarchy positions
for c in range(len(hierarchy)):
    try: hierarchyPositions[c] = order.index(hierarchy[c])
    except: pass

print("pre-hierarchy:", hierarchy)
print("pre-hierarchyPositions:", hierarchyPositions)

# Find first index
if hierarchyPositions[-1] == -1:
    for i in range(len(order)-1, -1, -1):
        if order[i] == 0:
            order[i] = hierarchy[-1]
            hierarchyPositions[-1] = i
            break
print("updated last hp:", hierarchyPositions)
print("before rest of hp, order changed to: %s\n" % order)

for i in range(M-2, -1, -1):
    if hierarchyPositions[i] != -1: continue
    print("moving i: %s, h: %s, hp: %s, prev was: %s" % (i, hierarchy[i], hierarchyPositions[i], hierarchyPositions[i+1]))
    for j in range(hierarchyPositions[i+1]-1, -1, -1):
        print("looking at index %s" % j)
        if order[j] == 0:
            order[j] = hierarchy[i]
            break
    print("order changed to: %s\n" % order)

pos = -2
try:
    pos = order.index(1)
except:
    for i in range(N):
        if order[i] == 0:
            pos = i
            break

print("order", order)
print("hierarchyPositions", hierarchyPositions)

with open("milkorder.out", "w") as f:
    f.write("%s\n" % (pos + 1))