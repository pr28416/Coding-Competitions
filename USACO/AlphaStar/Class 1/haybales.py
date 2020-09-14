# use binary search for each part of each query

def lb_binsearch(lst, x):
    lo, up = 0, len(lst)
    while lo < up:
        y = lo + (up - lo) // 2
        if lst[y] >= x: up = y
        else: lo = y+1
    return lo

def ub_binsearch(lst, x):
    lo, up = 0, len(lst)
    while lo < up:
        y = lo + (up - lo) // 2
        if lst[y] > x: up = y
        else: lo = y+1
    return lo

# N, Q = map(int, input().split(" "))
# positions = sorted(list(map(int, input().split(" "))))
# queries = [list(map(int, input().split(" "))) for _ in range(Q)]

# for query in queries:
#     print(ub_binsearch(positions, query[1]) -
#             lb_binsearch(positions, query[0]))

with open("haybales.in") as f:
    N, Q = map(int, f.readline().split(" "))
    positions = sorted(list(map(int, f.readline().split(" "))))
    queries = [list(map(int, f.readline().split(" "))) for _ in range(Q)]

with open("haybales.out", "w") as f:
    for query in queries:
        f.write("%s\n" % (
            ub_binsearch(positions, query[1]) -
            lb_binsearch(positions, query[0])
            ))