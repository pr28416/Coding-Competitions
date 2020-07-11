N, logs = 0, []
with open("taming.in", "r") as f:
    N = int(f.readline())
    logs = [int(i) for i in f.readline().split(" ")]

# 0 = breakout
# 1 = no breakout
# 2 = either

breakouts = [0] * len(logs)
i = len(breakouts)-1
while i >= 0:
    if logs[i] == 0:
        i -= 1
        # print(breakouts)
        continue
    if logs[i] > 0:
        j, e = 0, i
        while i >= 0 and j < logs[e]:
            if logs[e - j] == -1 or logs[e - j] == logs[e] - j:
                breakouts[i] = 1
                i -= 1
                j += 1
            else:
                with open("taming.out", "w") as f:
                    f.write("-1\n")
                    import sys
                    sys.exit()
        if i >= 0:
            breakouts[i] = 0
            i -= 1
        # print(breakouts)
        continue
    if logs[i] < 0:
        breakouts[i] = 2
        i -= 1
        # print(breakouts)
        continue

print("original", logs)
print("breakouts", breakouts)

if breakouts[0] != 0 and breakouts[0] != 2:
    with open("taming.out", "w") as f:
        f.write("-1\n")
else:
    breakouts[0] = 0
    maxBreakouts, minBreakouts = 0, 0
    
    for i in breakouts:
        if i == 0:
            minBreakouts += 1
    for i in breakouts:
        if i == 0 or i == 2:
            maxBreakouts += 1
    # print(minBreakouts, maxBreakouts)
    with open("taming.out", "w") as f:
        f.write("%s %s\n" % (minBreakouts, maxBreakouts))

# [0, -1, 1, 0, 1, 2, -1, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]