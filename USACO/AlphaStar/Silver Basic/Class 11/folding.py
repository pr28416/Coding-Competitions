N, L = map(int, input().split(" "))
knots = [0]*(2*L+1)
for _ in range(N): knots[int(input())*2] = 1
for i in range(1, len(knots), 2): knots[i] = 2

count = 0
for i in range(1, len(knots)-1):
    dist = min(i, len(knots)-1-i)
    lo, up = i-dist, i+dist+1
    if knots[lo:i] == knots[up-1:i:-1]: count += 1
print(count)