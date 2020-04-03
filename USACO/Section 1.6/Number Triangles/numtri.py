"""
ID: pranav.19
LANG: PYTHON3
TASK: numtri
"""

N = 0
triangle = []
with open("numtri.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        triangle.append([int(i) for i in f.readline().split(" ")])

for i, a in enumerate(triangle):
    for k in range(N-i-1):
        a.append(0)

for row in range(N-1, -1, -1):
    for pos in range(len(triangle[row])-1):
        if triangle[row][pos] > triangle[row][pos+1]:
            triangle[row-1][pos] += triangle[row][pos]
        else:
            triangle[row-1][pos] += triangle[row][pos+1]

with open("numtri.out", "w") as f:
    f.write("%s\n" % triangle[0][0])
