N = 0
clocks = []
blueprint = []
initial = []
import sys
with open("clocktree.in", "r") as f:
    N = int(f.readline())
    clocks = [int(i) for i in f.readline().split(" ")]
    for i in range(N-1):
        initial.append([int(i) for i in f.readline().split(" ")])
    blueprint = [[0 for a in range(N)] for b in range(N)]


for i in initial:
    blueprint[i[0]-1][i[1]-1] = 1
    blueprint[i[1]-1][i[0]-1] = 1

loc = []

sys.setrecursionlimit(2000)

def span(start, depth, cks):
    global clocks
    print("  "*depth+"@%s %s" % (start, cks))
    if cks == clocks and depth != 0:
        return
    for i in cks:
        if i != 0:
            break
    else:
        loc.append(start)
        return

    for i in range(len(cks)):
        if blueprint[start][i] == 1 and i != start:
            prev = cks[i]
            cks[i] = (cks[i] + 1) % 12
            span(i, depth+1, cks)
            cks[i] = prev

for i in range(N):
    span(i, 0, clocks)

print("final", loc)
with open("clocktree.out", "w") as f:
    f.write("%s\n" % len(loc))