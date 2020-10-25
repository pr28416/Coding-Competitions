N = int(input())
weights = sorted([int(input()) for _ in range(N)], reverse=True)

def satisfies(a, b):
    for i in range(1, min(len(str(a)), len(str(b)))+1):
        if int(str(a)[-i]) + int(str(b)[-i]) >= 10:
            return False
    return True

fcount = 0
def recurse(i, csum, c):
    global N, weights, fcount
    if i == N:
        if c > fcount: fcount = c
    else:
        if satisfies(csum, weights[i]):
            recurse(i+1, csum+weights[i], c+1)
        recurse(i+1, csum, c)

recurse(0, 0, 0)
print(fcount)