with open('cownomics.in') as f:
    N, M = map(int, f.readline().split(" "))
    spotty = [f.readline().strip("\n") for _ in range(N)]
    plain = [f.readline().strip("\n") for _ in range(N)]

# print(N, M)
# print(spotty)
# print(plain)

def conv(n):
    return {'A': 0, 'C': 1, 'G': 2, 'T': 3}[n]

count = 0
for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            marked = [0] * 64
            for s in spotty:
                marked[16*conv(s[i])+4*conv(s[j])+conv(s[k])] = 1
            shouldBreak = False
            for p in plain:
                if marked[16*conv(p[i])+4*conv(p[j])+conv(p[k])]:
                    shouldBreak = True
                    break
            if shouldBreak: continue
            count += 1

with open('cownomics.out', 'w') as f:
    # print(count)
    f.write("%s\n" % count)