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

# print("sorted\t",*sorted)
# print("numbers\t",*numbers)
count = 0
while numbers != sorted:
    differences = [sorted[i]-numbers[i] for i in range(N)]
    for i in range(N):
        if differences[i] == 0:
            differences[i] = -4
    # Get max index and switch index
    maxIdx = differences.index(max(differences))
    # switchIdx = numbers.index(sorted[maxIdx])
    switchIdx = 0
    for i in range(N):
        if numbers[i] == sorted[maxIdx] and differences[i] != -4:
            switchIdx = i
            break

    # Perform the switch
    # print("(%s)<->(%s)\t" % (maxIdx, switchIdx), *numbers)
    numbers[maxIdx], numbers[switchIdx] = numbers[switchIdx], numbers[maxIdx]
    count += 1

# print("final\t", *numbers)
# print("steps: %s" % count)

with open("sort3.out", "w") as f:
    f.write("%s\n" % count)