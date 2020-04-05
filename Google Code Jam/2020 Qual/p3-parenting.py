T = int(input())

def split(x):
    if len(x) == 1:
        return x
    
    a = split(x[:len(x)//2])
    b = split(x[len(x)//2:])
    return merge(a, b)

def merge(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][0] < b[0][0]:
            x.append(a.pop(0))
        elif a[0][0] > b[0][0]:
            x.append(b.pop(0))
        else:
            if a[0][1] < b[0][1]:
                x.append(a.pop(0))
            else:
                x.append(b.pop(0))
    
    while len(a) > 0:
        x.append(a.pop(0))

    while len(b) > 0:
        x.append(b.pop(0))

    return x

def split2(x):
    if len(x) == 1:
        return x
    
    a = split(x[:len(x)//2])
    b = split(x[len(x)//2:])
    return merge2(a, b)

def merge2(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][2] < b[0][2]:
            x.append(a.pop(0))
        else:
            x.append(b.pop(0))
    
    while len(a) > 0:
        x.append(a.pop(0))

    while len(b) > 0:
        x.append(b.pop(0))

    return x


# Backtracking
workingSols = set()
didWork = False

def recurse(used, sortedTimes, normalTimes):
    """
    Algorithm (requires sortedTimes, set of working solutions):
    - Start with first interval in a list
    - For every interval from last item in list onwards:
        - Pick that item and search it
        - Merge recursion result to set of working solutions
        - Take the item out
    - If could not pick an interval, check this solution to see if it works
    - If solution works, add to set of working solutions
    """
    global workingSols
    didChange = False
    # print(used)
    for interval in range(used[len(used)-1]+1, len(sortedTimes)):
        if sortedTimes[interval][0] >= sortedTimes[used[len(used)-1]][1]:
            didChange = True
            used.append(interval)
            recurse(used, sortedTimes, normalTimes)
            del used[len(used)-1]
    
    if not didChange:
        e = sortedTimes.copy()
        for i in range(len(used)-1, -1, -1):
            del e[used[i]]
        
        for i in range(len(e)-1):
            if e[i][1] > e[i+1][0]:
                return

        p1Stuff = {sortedTimes[i] for i in used}
        fin = ""
        for i in normalTimes:
            if i not in p1Stuff:
                fin += "J"
            else:
                fin += "C"
        workingSols.add(fin)


def greedy(normalTimes, sortedTimes):
    maxTime = 0
    for t in times:
        if t[1] > maxTime:
            maxTime = t[1]

    workingTimes = [0 for i in range(maxTime+1)] # 0 --> ending activity's start
    # print(workingTimes[len(workingTimes)-1])
    # startTimes = {i[0] for i in times}

    for i in times:
        for j in range(i[0], i[1]):
            workingTimes[j] += 1

    for i in workingTimes:
        if i > 2:
            return "IMPOSSIBLE"
    # Add p1 times
    # print("before:", sortedTimes)
    p1Times = [sortedTimes.pop()]
    for i in range(len(sortedTimes)-1, -1, -1):
        if sortedTimes[i][1] <= p1Times[len(p1Times)-1][0]:
            p1Times.append(sortedTimes.pop(i))

    # print("after:", sortedTimes)
    # Verify that p2 times still work
    for i in range(len(sortedTimes)-1):
        if sortedTimes[i][1] > sortedTimes[i+1][0]:
            # return "IMPOSSIBLE"
            raise Exception("Program determined a possible solution to be impossible. Fix it.")

    d = {}
    for i in p1Times:
        d[i] = "C"
    fin = ""
    for i in normalTimes:
        if i not in d.keys():
            fin += "J"
        else:
            fin += "C"
    
    return fin


# Run tests
for t in range(T):
    N = int(input())
    times = []
    for n in range(N):
        f = tuple(int(i) for i in input().split(" "))
        times.append(f)

    sortedTimes = split(times)
    # print(sortedTimes)
    # # e = test2(times)
    # test3([0], sortedTimes)
    # d = {}
    workingSols = set()
    recurse([0], sortedTimes, times)

    # print("All solutions: %s" % workingSols)

    ans = "IMPOSSIBLE" if len(workingSols) == 0 else workingSols.pop()
    
    print("Case #%s: %s" % (t+1, ans))
    a = []
    didWork = False