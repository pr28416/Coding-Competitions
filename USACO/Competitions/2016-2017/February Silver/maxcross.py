with open("maxcross.in") as f:
    N, K, B = map(int, f.readline().split(" "))
    signals = [1] * (N+1)
    signals[0] = 0
    for _ in range(B):
        signals[int(f.readline())] = 0
    sums = [0] * (N+1)
    for i in range(1, N+1):
        sums[i] = sums[i-1] + signals[i]

print(N, K, B)
print(signals)
print(sums)

def simulate(k):
    global sums, K
    for i in range(K, N+1):
        if sums[i]-sums[i-K]+k >= K:
            return True
    return False

def search():
    lo, up = 0, K
    while lo < up:
        y = (lo+up)//2
        if simulate(y): up=y
        else: lo=y+1
    return lo

with open("maxcross.out", "w") as f:
    f.write("%s\n" % search())