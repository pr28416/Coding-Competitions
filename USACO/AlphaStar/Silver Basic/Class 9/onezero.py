N = int(input())
c = 0

def recurse(n, i, a, b):
    global N, c
    if i == N:
        print("".join([str(i) for i in n]))
        c += 1
    else:
        if b < (N-1)//2:
            recurse(n, i+1, a, b+1)
        n[i] = 1
        recurse(n, i+1, a+1, b)
        n[i] = 0

recurse([0] * N, 0, 0, 0)
print(c)