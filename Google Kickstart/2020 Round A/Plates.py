def crawl(N, K, prefixes, remaining, beauty, pIdx):
    if remaining == 0:
        # print("  "*pIdx, "happened properly")
        return beauty
    elif pIdx == N:
        # print("  "*pIdx, f"wasn't supposed to happen, remaining: {remaining}")
        return 0
        # return beauty
    else:
        maxBeauty = 0

        if pIdx == N-1:
            if remaining >= K:
                # print("  "*pIdx, "Not enough - returning")
                return 0
            # print("  "*pIdx, f"stack {pIdx}, K: {K}, remaining: {remaining}, taking all remaining")
            # print("  "*pIdx, f"beauty: {beauty} + {prefixes[pIdx][remaining]} -> {beauty+prefixes[pIdx][remaining]}")
            maxBeauty = max(maxBeauty, crawl(N, K, prefixes, 0, beauty+prefixes[pIdx][remaining], pIdx+1))
        else:
            # print("  "*pIdx, f"stack {pIdx}, K: {K}, remaining: {remaining}, starting at {0}, ending before {min(remaining, K)}")
            for i in range(0, min(remaining, K)):
                # print("  "*pIdx, f"stack {pIdx} take {i}, beauty: {beauty} + {prefixes[pIdx][i]} -> {beauty+prefixes[pIdx][i]}")
                maxBeauty = max(maxBeauty, crawl(N, K, prefixes, remaining-i, beauty+prefixes[pIdx][i], pIdx+1))

        return maxBeauty

def solve(T, N, K, P, plates):
    # print(N, K, P)
    prefixes = []

    # print("plates:")
    for p in plates:
        # print(p)
        prefixes.append([0] * (K+1))
        for i in range(1, K+1):
            prefixes[-1][i] = prefixes[-1][i-1] + p[i]

    # print("prefixes:")
    # for p in prefixes:
        # print(p)

    answer = crawl(N, K+1, prefixes, P, 0, 0)
    print(f"Case #{T}: {answer}")

for T in range(int(input())):
    N, K, P = map(int, input().split(" "))
    solve(T+1, N, K, P, [[0] + list(map(int, input().split(" "))) for _ in range(N)])