N = G = 0
cows = {}
logs = []
with open("measurement.py") as f:
    N, G = map(int, f.readline().split(" "))
    cows[0] = G # Cow 0 represents all other cows
    for i in range(N):
        logs.append(list(map(int, f.readline().split(" "))))
        cows[logs[-1][1]] = G

# Day 1: 10 12 10 10
# Day 4: 10 