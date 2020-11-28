N = int(input())
intervals = sorted([list(map(int, input().split(" "))) for _ in range(N)])
i = 0
while i < len(intervals)-1:
    if intervals[i][1] >= intervals[i+1][0]:
        if intervals[i][1] < intervals[i+1][1]:
            intervals[i][1] = intervals[i+1][1]
        del intervals[i+1]
    else: i += 1

total = 0
for i in intervals: total += i[1]-i[0]
print(total)