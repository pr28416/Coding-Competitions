fenceRanges = []

fenceRanges.append(list(map(int, input().split(" "))))
fenceRanges.append(list(map(int, input().split(" "))))

if fenceRanges[1][0] < fenceRanges[0][0]:
    fenceRanges[0], fenceRanges[1] = fenceRanges[1], fenceRanges[0]

if fenceRanges[0][1] >= fenceRanges[1][0]:
    if fenceRanges[0][1] > fenceRanges[1][1]:
        del fenceRanges[1]
    else:
        fenceRanges = [[fenceRanges[0][0], fenceRanges[1][1]]]

total = 0
for i in fenceRanges:
    total += i[1] - i[0]

print(total)
