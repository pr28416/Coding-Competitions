def isEquiv(a, b):
    if len(str(a)) != len(str(b)): return False
    c = str(b)
    while True:
        c = c[-1] + c[:len(c)-1]
        # print(c,a,b)
        if c == str(a): return True
        if c == str(b): return False

T = int(input())
for _ in range(T):
    e = input().split(" ")
    print("YES" if isEquiv(*map(int, e)) else "NO")