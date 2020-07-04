"""
ID: pranav.19
LANG: PYTHON3
TASK: beads
"""
# import time, logging, sys
# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
# logging.debug("Start")
N = 0
beads = []
with open("beads.in", "r") as f:
    N = int(f.readline())
    beads = [i for i in f.readline()]

maxBeads = 0

for b in range(len(beads)):
    temp = beads.copy()
    rightCount = 1
    leftCount = 1
    rShift = True
    lShift = True
    proceed = True
    while rShift == True:
        rShift = False
        if temp[b] == temp[(b+rightCount) % N]:
            rightCount += 1
            rShift = True
        elif temp[(b+rightCount) % N] == "w":
            temp[(b+rightCount) % N] = temp[b]
            rShift = True
        elif temp[b] == "w":
            for i in range(b, b+N):
                if temp[i % N] != "w":
                    temp[b] = temp[i % N]
                    rShift = True
                    break
            else:
                maxBeads = N
                break
        if rightCount == N:
            proceed = False
            rightCount = N-1
            break

    temp = beads.copy()
    if proceed == True:
        while lShift == True:
            lShift = False
            if temp[(b-1) % N] == temp[(b-leftCount-1) % N]:
                leftCount += 1
                lShift = True
            elif temp[(b-leftCount-1) % N] == "w":
                temp[(b-leftCount-1) % N] = temp[(b-1) % N]
                lShift = True
            elif temp[(b-1) % N] == "w":
                for i in range(b-1, b-N-1, -1):
                    if temp[i % N] != "w":
                        temp[(b-1) % N] = temp[i % N]
                        lShift = True
                        break
                else:
                    maxBeads = N
                    break

    if maxBeads < leftCount + rightCount:
        maxBeads = leftCount + rightCount

with open("beads.out", "w") as f:
    f.write(str(maxBeads)+"\n")

# logging.debug("Done")

"""
1) Pick an index i, set that to the bead type
2) Check if i+1 equals i or "w"
3) if yes then i+1 = i; go to 1
4) else check if i = "w"
5) if yes then i+1 = i; go to 1
6) else stop
"""

