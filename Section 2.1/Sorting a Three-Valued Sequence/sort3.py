"""
ID: pranav.19
LANG: PYTHON3
TASK: sort3
"""

N, numbers = 0, []

with open("sort3.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        numbers.append(int(f.readline()))

sorted = numbers.copy()
sorted.sort()
extras = numbers.copy()
extras = [extras[i] for i in range(len(extras)-1, -1, -1)]
backwards = extras.copy()
backwards.sort()
backwards.reverse()

# print(N)
#
print(*backwards)
print(*extras)
print("Starting")
swapCount = 0
backupCount = 0

for i in range(N-1):
    if numbers[i] != sorted[i]:
        # Get first index of correct item
        correctIdx = numbers.index(sorted[i], i)
        # Perform swap
        # print(*numbers, "swap (%s) %s <---> (%s) %s" % (i, numbers[i], correctIdx, numbers[correctIdx]))
        numbers[i], numbers[correctIdx] = numbers[correctIdx], numbers[i]
        # Increment swap count
        swapCount += 1
    if extras[i] != backwards[i]:
        # Get first index of correct item
        correctIdx = extras.index(backwards[i], i)
        # Perform swap
        print(*extras, "swap (%s) %s <---> (%s) %s" % (i, extras[i], correctIdx, extras[correctIdx]))
        extras[i], extras[correctIdx] = extras[correctIdx], extras[i]
        # Increment swap count
        backupCount += 1

print("Final")
print(*numbers)
print(backupCount, swapCount)

finalCount = backupCount
if swapCount < backupCount:
    finalCount = swapCount

with open("sort3.out", "w") as f:
    f.write("%s\n" % finalCount)