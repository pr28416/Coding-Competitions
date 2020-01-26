"""
ID: pranav.19
LANG: PYTHON3
TASK: subset
"""
from math import ceil
N = 0
answer = 0
with open("subset.in", "r") as f:
    N = int(f.readline())

allSets = []
masterSet = {i for i in range(1, N+1)}
masterSum = sum(masterSet)
req = N*(N+1)//4

def addSet(s): # Runtime: len(s) --> max: N
    global masterSet
    t = masterSet-s
    allSets.append(s)
    allSets.append(t)

def getRemainingSet(s): # Runtime: len(s) --> max: N
    global masterSum, masterSet, req
    # print(ceil(max(s)/2))
    # if ceil((req-sum(s))/2) == 0:
        # print("problem discovered")
    ret = {i for i in range(1, min(s)) if req-sum(s)-i >= 0 and i not in s}
    # print(len(ret))
    return ret

def compare(s):
    global req, allSets, used
    # Get values that can be used
    e = getRemainingSet(s)
    print("s:", *s, "\t\te:", *e)
    # print(s)
    if sum(s) == req and s not in allSets: # Runtime: N
        print("\tadd to allSets")
        allSets.append(s)
    elif len(e) == 0:
        print("\treturn, len == 0")
        return
    else:
        # Iterate through all the remaining ones
        for i in e: # Runtime: N
            compare(s | {i})
        
        # print("change by adding %s" % s)
# print((N*(N+1)//2))
if (N*(N+1)//2) % 2 != 1:
    # print("Each should add up to", req)
    # print(*masterSet)

    for i in range(max(masterSet)-1, (max(masterSet)-1)//2, -1):
        s = {N, i}
        # print(*s, end=" --> ")
        print("------------------------\n\tStarting %s\n------------------------" % i)
        compare(s)
    # compare({N})
        
answer = len(allSets)
with open("subset.out", "w") as f:
    # print("Final:", answer)
    # for i in allSets:
    #     print(*i)
    f.write("%s\n" % answer)