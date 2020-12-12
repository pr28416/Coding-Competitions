from heapq import heapify, heappush as hpush, heappop as hpop

with open('cowdance.in') as f:
    N, T = map(int, f.readline().split(" "))
    cows = [int(f.readline()) for _ in range(N)]

def simulate(k):
    global N, T, cows
    heap = cows[:k]
    heapify(heap)
    for i in range(k, N):
        new = hpop(heap) + cows[i]
        if new > T: return False
        hpush(heap, new)
    return True

def search():
    global N
    lo, up = 0, N
    while lo < up:
        y = (lo+up)//2
        if simulate(y): up=y
        else: lo=y+1
    return lo
    

with open('cowdance.out', 'w') as f:
    f.write("%s\n" % search())