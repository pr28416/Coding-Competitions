N = 0
cows = []
with open("hoofball.in", "r") as f:
    N = int(f.readline())
    cows = sorted([int(i) for i in f.readline().split(" ")])
    print(cows)

def getClosestPairs(cows):
    d = {}
    for p1 in range(len(cows)):
        p2 = 0
        for i in range(len(cows)):
            if i == p1: continue
            a = abs(cows[i]-cows[p1])
            b = abs(cows[p2]-cows[p1])
            if (a == 0 or b == 0) or (a < b and i != p1): p2 = i
        d[cows[p1]] = cows[p2]
    return d

pairs = getClosestPairs(cows)

sets = []
for i in cows:
    s = {i}
    last = i
    while pairs[last] not in s:
        e = pairs[last]
        s.add(pairs[last])
        last = e
    sets.append(s)

print("before:", *sets)
i = 0
while i < len(sets)-1:
    if sets[i] | sets[i+1] == sets[i]:
        del sets[i+1]
    elif sets[i] | sets[i+1] == sets[i+1]:
        del sets[i]
    else:
        i += 1
# print("after:", *sets)
with open("hoofball.out", "w") as f:
    f.write("%s\n" % len(sets))