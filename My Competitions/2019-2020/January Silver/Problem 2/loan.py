N, K, M = 0, 0, 0
with open("loan.in", "r") as f:
    t = f.readline().split(" ")
    N, K, M = int(t[0]), int(t[1]), int(t[2])

# print(N, K, M)

def payBackMethod(N, G, X):
    Y = (N-G)//X
    if Y < M:
        Y = M
    return Y

runTimes = []

def checkSolution(X):
    global runTimes
    global K
    global N
    total = 0
    dayCount = 1
    a = 0
    while total < N and dayCount <= K:
        a += 1
        # print("\t\tsubtracting")
        total += payBackMethod(N, total, X)
        dayCount += 1
    runTimes.append(a)
    # print("ran %s steps" % a)
    return total >= N

def newCheck(x):
    global runTimes, N, K, M
    totalPaid = 0
    daysElapsed = 1
    q = 0
    while totalPaid < N and daysElapsed <= K:
        # print("paid %s so far" % totalPaid)
        q += 1
        a = payBackMethod(N, totalPaid, x)
        totalPaid += a
        if a == M:
            if (K-daysElapsed)*M+totalPaid >= N:
                runTimes.append(q)
                return True
            else:
                runTimes.append(q)
                return False
        
        else:
            runTimes.append(q)
            
            if (K-daysElapsed) * M + totalPaid >= N:
                return True
            daysElapsed += 1
            
    return totalPaid >= N

def binarySearchThrough(l):
    global N
    x = len(l)//2
    # Check if middle works
    # print("checking: %s" % (l))
    # print("checking", end="\t")
    if checkSolution(l[x]):
        if not checkSolution(l[x]+1):
            return l[x]
        else:
            # Solution is greater
            return binarySearchThrough(l[x+1:])
    else:
        # Check left
        return binarySearchThrough(l[:x])

steps = 0
def testBinary(l):
    global N
    global steps
    st, end = 0, len(l)
    x = len(l[st:end])//2
    # print("Start x as %s" % x)
    # Check if middle works
    # print("checking: %s" % (l))
    # print("checking", end="\t")
    a, b = newCheck(l[x]), newCheck(l[x+1])
    while True:
        
        steps += 1
        # print("x: %s, checking through %s:%s" % (x, st, end))
        if a:
            if not b:
                return l[x]
            else:
                # Solution is greater
                
                st = x+1
        else:
            # Solution is less
            end = x
        x = (st+end)//2
        a, b = newCheck(l[x]), newCheck(l[x+1])
        

# G = 0
# for i in range(5):
#     G = payBackMethod(N, G, 3)
#     print(G)

# print(checkSolution(10000000))

weif = [i for i in range(N)]
a = testBinary(weif)
with open("loan.out", "w") as f:
    f.write("%s\n" % a)
print("newChecks max steps:", max(runTimes))
# print("steps:", steps)
# print(binarySearchThrough([i for i in range(N)]))
