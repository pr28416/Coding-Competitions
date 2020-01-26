"""
ID: pranav.19
LANG: PYTHON3
TASK: subset
"""

N = 0
answer = 0
with open("subset.in", "r") as f:
    N = int(f.readline())

def printDP(dp):
    for i in dp:
        for j in i:
            print(j, end="\t")
        print()

allSets = set()

def span(dp, node, totalSum, currentSet):
    # Check to see if 0 is the current spot. If so, add the currentSet to allSets
    if dp[node][totalSum] == 0:
        if sum(currentSet) == N*(N+1)//4:
            allSets.add(tuple(currentSet))
        return

    # Check to see if you can traverse left
    if dp[node][totalSum] >= node:
        # Span left, add number to currentSet
        mod = currentSet.copy()
        mod.add(node)
        span(dp, node, totalSum-node, mod.copy())
        del mod
    
    # Check to see if you can traverse up
    if node-1 >= 0 and dp[node][totalSum] == dp[node-1][totalSum]:
        # Span up
        span(dp, node-1, totalSum, currentSet.copy())

if (N*(N+1))//2 % 2 == 0:

    req = (N*(N+1))//4

    # PART 1: Create the dp 2d array
    dp = [[-1 for i in range(req+1)] for j in range(N+1)]

    # PART 2: Set the values of each DP position
    for node in range(N+1):
        for totalSum in range(req+1):
            # Values that are seen
            seenValues = [i for i in range(node+1)]
            
            # Check to see what value can be put in the box
            if sum(seenValues) > totalSum:
                dp[node][totalSum] = totalSum
            else:
                dp[node][totalSum] = sum(seenValues)
                break

    # PART 3: Starting from the bottom-right corner, create sets
    span(dp, N, req, set())

    # for i in allSets:
    #     print(i)
    print(len(allSets)//2)