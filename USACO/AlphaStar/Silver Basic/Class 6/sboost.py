import math
F, M, N = map(int, input().split(" "))
parts = [tuple(map(int, input().split(" "))) for _ in range(N)]
# for i in parts: print(i)

used = [0] * N
buckets = [None] * N
prev_idx = None

while True:
    l_idx = 0
    for i in range(len(used)):
        if used[i]: continue

        prev = (F, M) if prev_idx is None else buckets[prev_idx]
        buckets[i] = (prev[0]+parts[i][0], prev[1]+parts[i][1])

        if buckets[i][0]/buckets[i][1] > buckets[l_idx][0]/buckets[l_idx][1]:
            l_idx = i
        
    prev = (F, M) if prev_idx is None else buckets[prev_idx]
    if used[l_idx] or prev[0]/prev[1] > buckets[l_idx][0]/buckets[l_idx][1]: break
    used[l_idx] = 1
    prev_idx = l_idx

found = False
for i in range(len(used)):
    if used[i]:
        found = True
        print(i+1)

if not found: print("NONE")