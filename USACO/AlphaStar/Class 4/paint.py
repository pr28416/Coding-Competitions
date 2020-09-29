N = int(input())
commands = [input().split(" ") for _ in range(N)]
moves = [int(i[0]) if i[1] == "R" else -int(i[0]) for i in commands]
del commands
# print(moves)

bounds = [0, 0]
span = [0, 0]
marker = 0
locs = []
for move in moves:
    marker += move
    span[1] = marker
    locs.append(sorted(span+bounds)[1:3])
    span[0] = span[1]
    if marker > bounds[1]: bounds[1] = marker
    elif marker < bounds[0]: bounds[0] = marker

locs.sort()
# for i in locs: print(i)

total = 0
i = 0
while i < len(locs):
    if i == len(locs)-1:
        total += locs[i][1]-locs[i][0]
        i += 1
    else:
        if locs[i][1] < locs[i+1][0]:
            total += locs[i][1]-locs[i][0]
            i += 1
        elif locs[i][1] >= locs[i+1][0] and locs[i][1] >= locs[i+1][1]:
            del locs[i+1]
        elif locs[i][1] >= locs[i+1][0]:
            locs[i][1] = locs[i+1][1]
            del locs[i+1]
        else: i += 1

# print("final")
# for i in locs: print(i)
print(total)