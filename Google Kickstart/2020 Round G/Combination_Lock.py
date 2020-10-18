T = int(input())
for s in range(T):
    W, N = map(int, input().split(" "))
    combinations = list(map(lambda x: int(x)-1, input().split(" ")))
    combinations.sort()
    entire = combinations + combinations
    differences = [0] * (len(entire)-1)
    for i in range(len(differences)):
        if entire[i+1] >= entire[i]: differences[i] = entire[i+1]-entire[i]
        else: differences[i] = entire[i+1]-entire[i]+N
    # print(entire)
    # print(differences)
    finlo, finup, fc = 0, W-2, 0
    for i in range(finlo, finup+1):
        fc += differences[i]
    lo, up = 0, W-2
    sc = fc
    # print("init fc", fc)
    while up < len(differences):
        # print(sc)
        if sc < fc:
            fc = sc
            finlo, finup = lo, up
        sc -= differences[lo]
        lo, up = lo+1, up+1
        if up == len(differences): break
        sc += differences[up]
    # print("max range:", finlo, finup, fc)
    # print("captured", entire[finlo:finup+2])
    sub = entire[finlo:finup+2]
    for i in range(len(sub)-2, -1, -1):
        if sub[i] > sub[i+1]: sub[i] -= N
    # print(sub)
    avg = 0
    for i in sub: avg += i
    avg //= W
    # print("center around", avg)
    finSum = 0
    for i in sub: finSum += abs(i-avg)
    print("Case #{}: {}".format(s+1, finSum))

"""
[1, 8, 2, 7] mod 10 --> [1, 1, 1, 1] --> 8
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[_, *, *, _, _, _, _, *, *, _, _, *, *, _, _, _, _, *, *, _]
[7, 8, 9, 0, 1, 2]
[*, *, _, _, *, *] --> 8
    - [1, 2, 7, 8, 1, 2, 7, 8]
    -   1   5  1  3  1  5  1 --> [1, 2, 1] --> [7, 8, 1, 2]
center around average (-3, -2, 1, 2) --> 0
7 --> 3
8 --> 2
1 --> 1
2 --> 2

[1, 8, 2, 9, 4] mod 11
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[_, *, *, _, *, _, _, _, *, *, __, _, *, *, _, *, _, _, _, *, *, __]
center around average (-3, -2, 1, 2, 4) --> 0
-3 --> 3
-2 --> 2
1 --> 1
2 --> 2
4 --> 4
"""