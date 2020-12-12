with open("helpcross.in") as f:
    C, N = map(int, f.readline().split(" "))
    chickenTimes = sorted([int(f.readline()) for _ in range(C)])
    cowIntervals = sorted([list(map(int, f.readline().split(" ")))[::-1] for _ in range(N)])

# print("chickens:", chickenTimes)
# for i in cowIntervals: print(i)

def bs(x, lst, comp):
    lo, up = 0, len(lst)
    while lo < up:
        y = (lo+up)//2
        if comp(x, lst[y]): up=y
        else: lo=y+1
    return lo

count = 0
for interval in cowIntervals:
    chicken = bs(interval[1], chickenTimes, lambda x, y: x <= y)
    if (chicken < len(chickenTimes) and chickenTimes[chicken] <= interval[0]):
        # print(f"Chicken i{chicken} ({chickenTimes[chicken]}) assigned to", interval)
        count += 1
        del chickenTimes[chicken]

# print(count)
with open("helpcross.out", "w") as f:
    f.write("%s\n" % count)

"""
chickens: [2, 6, 7, 8, 9]
[0, 3]      2
[2, 5]      2
[4, 9]      6, 7, 8, 9
[8, 13]     8, 9


2   [0, 3], [2, 5]
6   [4, 9]
7   [4, 9]
8   [4, 9], [8, 13]
9   [4, 9], [8, 13]
"""