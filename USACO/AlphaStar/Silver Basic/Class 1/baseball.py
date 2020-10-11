# Brute force cows i and j and upper-bound-bin-search cow k - answers for d2 will be between two numbers, so lb-search and ub-search the two numbers.

N = int(input())
cows = sorted([int(input()) for _ in range(N)])
# print(cows)
steps = 0

def lb_binsearch(lst, i, j):
    global steps
    lo, up = j+1, len(lst)
    while lo < up:
        steps += 1
        y = lo + (up - lo) // 2
        if lst[y]-lst[j] >= lst[j]-lst[i]: up = y
        else: lo = y+1
    return lo

def ub_binsearch(lst, i, j):
    global steps
    lo, up = j+1, len(lst)
    while lo < up:
        steps += 1
        y = lo + (up - lo) // 2
        if lst[y]-lst[j] <= 2*(lst[j]-lst[i]): lo = y+1
        else: up = y
    return lo

count = 0

for i in range(len(cows)-2):
    for j in range(i+1, len(cows)-1):
        ub = ub_binsearch(cows, i, j)
        lb = lb_binsearch(cows, i, j)
        # print(lb)
        # print(cows[i], cows[j], "..", cows[ub-1])
        if lb >= len(cows): break
        count += ub - lb

print(count)