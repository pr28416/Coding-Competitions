N, K, B = map(int, input().split(" "))
signals = [1]*N
for _ in range(B):
    signals[int(input())-1] = 0

print(signals)
sums = [signals[0]]
for i in range(1, N):
    sums.append(sums[i-1] + signals[i])

print(sums)

fin = N-B
for m in range(1, N-B+1):
    for i in range(N-K):
        e = sums[i+K]-(0 if i == 0 else sums[i-1])
        if e + m >= K:
            print(f"{m} worked: {i}-{i+K}, {e} + {m} = {e+m} >= {K}")
            fin = m+1; break
    else:
        print(m, "didn't work")
        continue
    break

print(fin)