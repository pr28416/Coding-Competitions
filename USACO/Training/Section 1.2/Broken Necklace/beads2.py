"""
1) Pick an index i, set that to the bead type
2) Check if i+1 equals i or "w"
3) if yes then i+1 = i; go to 1
4) else check if i = "w"
5) if yes then i+1 = i; go to 1
6) else stop
"""

N = 0
beads = []
with open("beads.in", "r") as f:
    N = int(f.readline())
    beads = [i for i in f.readline()]

maxBeads = 0

def g(i):
    return i % N


for i in range(29):
    # check right
    rightCount = 1
    beadType = "w"
    c = i
    while True:
        if beads[g(c)] == beads[g(c+1)] or beads[g(c+1)] == "w":
            rightCount += 1
            c = g(c+1)