N = int(input())
hills = sorted([int(input()) for _ in range(N)])

minCost = 100000000
for minH in range(84):
    maxH = minH + 17
    # print("checking from %s..%s" % (minH, maxH))
    cost = 0
    for hill in hills:
        if hill >= minH and hill <= maxH: continue
        elif hill < minH: cost += (minH - hill) ** 2
        elif hill > maxH: cost += (maxH - hill) ** 2
    if cost < minCost: minCost = cost

print(minCost)