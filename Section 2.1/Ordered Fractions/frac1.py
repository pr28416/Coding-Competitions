"""
ID: pranav.19
LANG: PYTHON3
TASK: frac1
"""

import time
st=time.time()

N = 0
with open("frac1.in", "r") as f:
    N = int(f.readline())

usedNumbers, usedStrings = [], []
for d in range(1, N+1):
    for n in range(d+1):
        if n/d not in usedNumbers:
            usedStrings.append("%s/%s" % (n, d))
            usedNumbers.append(n/d)

# ("%s/%s" % (n, d)) not in usedStrings and
total = []
for i in range(len(usedStrings)):
    total.append([usedStrings[i], usedNumbers[i]])


def split(x):
    if len(x) == 1:
        return x
    a = split(x[:int(len(x)/2)])
    b = split(x[int(len(x)/2):])
    return merge(a, b)

def merge(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][1] < b[0][1]:
            x.append(a.pop(0))
        else:
            x.append(b.pop(0))
    while len(a) > 0:
        x.append(a.pop(0))
    while len(b) > 0:
        x.append(b.pop(0))
    return x

total = split(total)
a = [i[0] for i in total]
# print(*a)

# print("Time elapsed: %.5f" % (time.time()-st))
with open("frac1.out", "w") as f:
    for i in a:
        f.write("%s\n" % i)