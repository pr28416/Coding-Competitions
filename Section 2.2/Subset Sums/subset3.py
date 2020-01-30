"""
ID: pranav.19
LANG: PYTHON3
TASK: subset
"""

n = 0
with open("subset.in", "r") as f:
    n = int(f.readline())

def printDP(dp):
    for i in dp:
        for j in i:
            print(j, end="\t")
        print()

allSets = set()
steps = 0

def span(dp, node, totalSum, currentSet):
    global n, steps
    # Check to see if 0 is the current spot. If so, add the currentSet to allSets
    # print("\nCurrently at (%s, %s)" % (node, totalSum))
    # print("Set is", currentSet)
    steps += 1
    if dp[node][totalSum] == 0:
        if sum(currentSet) == n*(n+1)//4:
            # print("Adding %s to allSets" % currentSet)
            allSets.add(tuple(currentSet))
        # else:
            # print("Did not add %s to allSets" % currentSet)
        return

    # Check to see if you can traverse left
    if dp[node][totalSum] >= node:
        # Span left, add number to currentSet
        mod = currentSet.copy()
        mod.add(node)
        # print("Spanning left to (%s, %s)" % (node, totalSum-node))
        span(dp, node, totalSum-node, mod.copy())
        del mod
    # elif dp[node][totalSum] + sum(currentSet) == n*(n+1)//4:
    #     print("ALERT")
    #     mod = currentSet.copy()
    #     mod.add(dp[node][totalSum])
    #     print("Adding %s to allSets" % mod)
    #     allSets.add(tuple(mod))
    #     return
    # else:
    #     print("Can't span left")
    
    # Check to see if you can traverse up, reduce over-counting by not checking multiple reqs
    if node-1 >= 0 and dp[node][totalSum] == dp[node-1][totalSum] and totalSum != n*(n+1)//4:
        # Span up
        # print("Spanning up to (%s, %s)" % (node-1, totalSum))
        span(dp, node-1, totalSum, currentSet.copy())
    # else:
    #     print("Can't span up")

def populate(N):
    answer = 0
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

        printDP(dp)
        print("%s by %s table" % (N, req))
        # PART 3: Starting from the bottom-right corner, create sets
        # allSets.clear()
        # span(dp, N, req, set())

        answer = len(allSets)//1
        # print("\n\nFINAL --> %s: %s" % (N, answer))
    else:
        print("%s: \\\\" % N)

    print("\nTotal steps:", steps)
    # for i in allSets:
    #     print(i)
    
    with open("subset.out", "w") as f:
        f.write("%s\n" % answer)

# for i in range(2, 10):
#     populate(i)
populate(n)