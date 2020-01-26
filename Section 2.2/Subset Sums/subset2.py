"""
ID: pranav.19
LANG: PYTHON3
TASK: subset
"""
from itertools import combinations

n = 0
with open("subset.in", "r") as f:
    n = int(f.readline())

# def generate(n, k):
#     master = [i for i in range(1, n+1)]
#     arr = []
#     for i in range(len(master), 1, -1):
#         t = master.copy()
#         s = set([])
#         a = i
#         for j in range(k):
#             s.add(a)
#             a -= 1
#         arr.append(s)
#     for i in arr:
#         print(i)

# generate(7, 3)

req = (n*(n+1))//4
c = 0
allSet = []
if (n*(n+1))//2 % 2 == 0:
    for i in range(1, n):
        a = list(combinations([k for k in range(1, n+1)], i))
        for combo in a:
            if sum(combo) == req:
                allSet.append(combo)
                c += 1

# print(c//2)
# print(*allSet)
with open("subset.out", "w") as f:
    f.write("%s\n" % (c//2))

