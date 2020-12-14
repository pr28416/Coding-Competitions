from collections import deque

with open('pairup.in') as f:
    N = int(f.readline())
    cows = []
    for _ in range(N):
        x, y = map(int, f.readline().split(" "))
        cows.append([y, x])
    cows.sort()
    cows = deque(cows)

maxTime = 0
while len(cows) > 1:
    left = cows.popleft()
    right = cows.pop()
    maxTime = max(maxTime, left[0]+right[0])
    if left[1] > right[1]:
        left[1] -= right[1]
        cows.appendleft(left)
    elif left[1] < right[1]:
        right[1] -= left[1]
        cows.append(right)

if len(cows) == 1:
    maxTime = max(maxTime, cows.pop()[0] * 2)

with open('pairup.out', 'w') as f:
    f.write("%s\n" % maxTime)