N, M = map(int, input().split(" "))
spotty = [input() for _ in range(N)]
plain = [input() for _ in range(N)]

count = 0
conv = dict(zip("ACGT", [0, 1, 2, 3]))

for i in range(M-2):
    for j in range(i+1, M-1):
        for k in range(j+1, M):
            marked = [0] * 64
            for s in spotty:
                marked[conv[s[i]]*16+conv[s[j]]*4+conv[s[k]]] = 1
            for s in plain:
                if marked[conv[s[i]]*16+conv[s[j]]*4+conv[s[k]]]: break
            else: count += 1

print(count)