N = int(input())
pairs = []
inverse = []
for _ in range(N):
    e = input().split(" ")
    pairs.append(e)
    inverse.append(e[::-1])

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
abv = [f"{i}{j}" for i in alpha for j in alpha]
matrix = [[0]*676 for _ in range(676)]
# print(abv)

def bs(x, lst, i, j, comp):
    lo, up = i, j
    while lo < up:
        y = lo+(up-lo)//2
        if comp(x, lst[y]): up = y
        else: lo = y+1
    return lo

pairs.sort()
inverse.sort()

# for i in pairs: print(i)
for pair in pairs:
    # print(pair)
    olo = bs(pair[1], pairs, 0, len(pairs), lambda x, y: x <= y[0][:2])
    oup = bs(pair[1], pairs, 0, len(pairs), lambda x, y: x < y[0][:2])
    # print(f"\t{pair} possible choices ({lo}:{up}): {pairs[lo:up]}")
    lo = bs(pair[0][:2], inverse, 0, len(pairs), lambda x, y: x <= y[0])
    up = bs(pair[0][:2], inverse, 0, len(pairs), lambda x, y: x < y[0])
    # print(f"\t{pair} narrowed down to ({lo}:{up}): {pairs[lo:up]}")
    if lo < up:
        print(f"\t{pair} narrowed down to ({lo}:{up}): {inverse[lo:up]}")
        i, j = bs(pair[0][:2], abv, 0, len(abv), lambda x, y: x <= y), bs(pair[1], abv, 0, len(abv), lambda x, y: x <= y)
        matrix[i][j] += up-lo
        # matrix[j][i] += up-lo
        # print(f"\tADDING pairs ({abv[i]},{abv[j]}) and ({abv[j]},{abv[i]})")

s = 0
for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        s += matrix[i][j]

print(s)