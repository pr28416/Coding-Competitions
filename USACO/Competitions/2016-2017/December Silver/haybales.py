from bisect import bisect_left as lb, bisect_right as ub

with open("haybales.in") as f:
    N, Q = map(int, f.readline().split(" "))
    bales = sorted(map(int, f.readline().split(" ")))
    queries = [list(map(int, f.readline().split(" "))) for _ in range(Q)]

with open("haybales.out", "w") as f:
    for (a, b) in queries:
        lower = lb(bales, a)
        upper = ub(bales, b)
        f.write(str(upper-lower)+"\n")
