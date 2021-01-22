N, M, K = map(int, input().split(" "))
desired = list(map(int, input().split(" ")))
sizes = list(map(int, input().split(" ")))
desired.sort()
sizes.sort()

d = s = c = 0
while d < N and s < M:
    if abs(sizes[s]-desired[d]) <= K:
        c += 1; d += 1; s += 1
    elif sizes[s] - desired[d] > K:
        d += 1
    else:
        s += 1

print(c)