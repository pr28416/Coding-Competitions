N = G = 0
cows = {}
logs = []
with open("measurement.in") as f:
    N, G = map(int, f.readline().split(" "))
    cows[0] = G
    cowIDs = set()
    for i in range(N):
        logs.append(list(map(int, f.readline().split(" "))))
        cows[logs[-1][1]] = G

logs.sort()
for i in cows: print(i, cows[i])

def binSearch(lst, x):
    lo, up = 0, len(lst)
    while lo < up:
        y = lo+(up-lo)//2
        if x <= lst[y]: up = y
        else: lo = y+1
    return lo

bestCows = [] # Maintains a sorted list of best cows
currentMax = None
count = 0
for log in logs:
    cows[log[1]] += log[2]
    print("changed %s to %s" % (log[1], cows[log[1]]))
    loc = binSearch(bestCows, log[1])

    # List is empty, or cow is added to end
    if currentMax == None or loc == len(bestCows) and cows[log[1]] >= currentMax:
        bestCows.append(log[1])
        currentMax = cows[log[1]]
        count += 1
        print("best cows:", bestCows)
        continue
    # Different cows
    if log[1] != bestCows[loc]:
        print("d")
        # Cow should be added to list
        if cows[log[1]] == currentMax:
            bestCows.insert(loc, log[1])
            count += 1
        # Cow should be the only one in the list
        elif cows[log[1]] > currentMax:
            bestCows = [log[1]]
            currentMax = cows[log[1]]
            count += 1
    # Same cows
    else:
        print("s")
        # Cow should be the only one
        if cows[log[1]] > currentMax:
            bestCows = [log[1]]
            currentMax = cows[log[1]]
            count += 1
        # Cow should be removed
        else:
            del bestCows[loc]
            count += 1

    print("best cows:", bestCows)
print(count)
with open("measurement.out", "w") as f:
    f.write("%s\n" % count)

# Day 1: 10 12 10 10
# Day 4: 10 12 9 10
# Day 7: 10 12 9 13
# Day 9: 10 12 9 12