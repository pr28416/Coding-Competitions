N, a, b, c, d, e, f, g, h, M = map(int, input().split(" "))
best = []
i = 0
while i < 3*N:
    i2= pow(i, 2)
    i3 = i2*i
    w = (i2%d*(a*i3+b)+c)%d
    u = (i3%h*(e*i2+f)+g)%h
    best.append((-u, w))
    i += 1
    # print(i)
# print(len(best))

for i in best: print(i)
best.sort()
s = 0
for i in range(N):
    s += best[i][1]
print(s%M)