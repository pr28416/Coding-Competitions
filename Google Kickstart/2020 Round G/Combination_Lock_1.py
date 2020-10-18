T = int(input())
for s in range(T):
    W, N = map(int, input().split(" "))
    combinations = list(map(lambda x: int(x)-1, input().split(" ")))
    combinations.sort()
    entire = combinations + [i+N for i in combinations]
    # print(entire)
    fdev = None
    for i in range(W):
        sub = entire[i:i+W]
        avg = sum(sub)//W
        dev = 0
        for i in sub: dev += abs(avg-i)
        if fdev is None or dev < fdev: fdev = dev
    print("Case #%s: %s" % (s+1, fdev))

# [1, 2, 7, 8, 11, 12, 17, 18]