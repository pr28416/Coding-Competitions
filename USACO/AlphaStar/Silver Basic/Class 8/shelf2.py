N, B = map(int, input().split(" "))
heights = sorted([int(input()) for _ in range(N)], reverse=True)
# print(N, B)
# print(heights)
maxDiff = None

def recurse(heights, i, csum, limit):
    global maxDiff
    if csum >= limit and (maxDiff is None or csum-limit < maxDiff):
        maxDiff = csum-limit
    else:
        for j in range(i, len(heights)):
            recurse(heights, j+1, csum+heights[j], limit)

recurse(heights, 0, 0, B)
print(maxDiff)