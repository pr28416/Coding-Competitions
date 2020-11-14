N = int(input())
temp = sorted([input().split(" ") for _ in range(N)], key=lambda x: int(x[0]))
nums = [0] + [int(t[0]) for t in temp]
cows = [''] + [t[1] for t in temp]
del temp
# print(nums)
# print(cows)

sums = [(0,0)] * (N+1)
for i in range(1, N+1):
    sums[i] = (sums[i-1][0]+1, sums[i-1][1]) if cows[i] == 'G' else (sums[i-1][0], sums[i-1][1]+1)
del cows
print(sums)
maxSize = 0
for k in range(N, 1, -1):
    for i in range(N-k+1):
        a = sums[i+k][0]-sums[i][0] == sums[i+k][1]-sums[i][1]
        b = sums[i+k][0]-sums[i][0] == 0
        c = sums[i+k][1]-sums[i][1] == 0
        if a or b or c:
            e = nums[i+k]-nums[i+1]
            if e > maxSize: maxSize = e
            # print(f"k: {k}, i:{i}, [{i+1},{i+k}], size={nums[i+k]-nums[i+1]}, nG:{sums[i+k][0]-sums[i][0]}, nH: {sums[i+k][1]-sums[i][1]}")
print(maxSize)

"""
H   H   H   G   G   G   G   H   H   G   G   G   H
5   6   7   10  11  15  20  21  22  30  40  100 110
[0, 3)      --> [5, 7]
[3, 7)
[7, 9)      --> [21, 22]
[11, 12)    --> [110, 110]
H: 2, 1, 0
G: 14, 88
H+G: (7-5+1, 21-7), (22-21+1, 110-22)

G   H   G   G   H   G
1   3   4   7   10  16
"""