# from collections import deque

def recurse(dq:list, Sum, Prod, i):
    global maxScore, primeSet
    if (i, Prod) in primeSet:
        # print("repeated")
        # print(Prod, 'here')
        return

    primeSet.add((i, Prod))
    if Sum == Prod:
        maxScore = max(maxScore, Sum)
    elif Prod > Sum:
        return
    if i >= len(dq):
        return
    else:
        recurse(dq, Sum-dq[i], Prod*dq[i], i+1)
        recurse(dq, Sum, Prod, i+1)


T = int(input())
maxScore = 0
primeSet = set()
for t in range(1, T+1):
    M = int(input())
    deck = []
    maxScore = 0
    primeSet.clear()
    for _ in range(M):
        inp = tuple(map(int, input().split(" ")))
        for _ in range(inp[1]):
            deck.append(inp[0])
    deck.sort()
    recurse(deck, sum(deck), 1, 0)
    print(f"Case #{t}: {maxScore}")
