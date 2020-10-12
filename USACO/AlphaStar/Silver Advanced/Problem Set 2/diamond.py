N, K = map(int, input().split(" "))
sizes = sorted([int(input()) for _ in range(N)])

leftSide, rightSide = [0] * N, [0] * N

j = 0
for i in range(N):
    if i == 0: leftSide[i] = 1; continue
    while j < i and sizes[i]-sizes[j] > K: j += 1
    leftSide[i] = max(i-j+1, leftSide[i-1])

j = N-1
for i in range(N-1, -1, -1):
    if i == N-1: rightSide[i] = 1; continue
    while j > i and sizes[j]-sizes[i] > K: j -= 1
    rightSide[i] = max(j-i+1, rightSide[i+1])

s = 0
for i in range(N):
    if leftSide[i]+rightSide[i] > s:
        s = leftSide[i]+rightSide[i]

print(min(s, N))