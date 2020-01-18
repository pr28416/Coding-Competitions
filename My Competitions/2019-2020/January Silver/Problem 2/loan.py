N, K, M = 0, 0, 0
with open("loan.in", "r") as f:
    t = f.readline().split(" ")
    N, K, M = int(t[0]), int(t[1]), int(t[2])

print(N, K, M)

def payBackMethod(N, G, X):
    Y = (N-G)//X
    if Y < M:
        Y = M
    return Y

def checkSolution(X):
    global K
    global N
    total = 0
    dayCount = 1
    while total < N and dayCount <= K:
        # print("\t\tsubtracting")
        total += payBackMethod(N, total, X)
        dayCount += 1
    return total >= N

def binarySearchThrough(l):
    global N
    x = len(l)//2
    # Check if middle works
    # print("checking: %s" % (l))
    print("checking", end="\t")
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
    a, b = checkSolution(l[x]), checkSolution(l[x+1])
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
        x = len(l[st:end])//2
        a, b = checkSolution(l[x]), checkSolution(l[x+1])

# G = 0
# for i in range(5):
#     G = payBackMethod(N, G, 3)
#     print(G)

# print(checkSolution(10000000))
print(testBinary([i for i in range(N)]))
print("steps:", steps)
# print(binarySearchThrough([i for i in range(N)]))
