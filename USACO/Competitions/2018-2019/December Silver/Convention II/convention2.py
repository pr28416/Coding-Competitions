with open("convention2_1.in") as f:
    N = int(f.readline())
    waitingLine = [list(map(int, f.readline().split(" "))) for _ in range(N)]
    for t in range(N):
        waitingLine[t].append(t+1)

waitingLine.sort(reverse=True, key=lambda x: (x[0], x[2]))
steps = 0

def bs(x, lst, comp):
    # global steps
    lo, up = 0, len(lst)
    while lo < up:
        # steps += 1
        y=(lo+up)//2
        if comp(x, lst[y]): up=y
        else: lo=y+1
    return lo

primaryLine = []
answer = 0
time = waitingLine[-1][0]

while len(waitingLine) > 0:
    # steps += 1
    cur = primaryLine.pop() if len(primaryLine) > 0 else waitingLine.pop()
    time += cur[1]
    while len(waitingLine) > 0 and waitingLine[-1][0] < time:
        # steps += 1
        item = waitingLine.pop()
        primaryLine.insert(bs(item, primaryLine, lambda x, y: x[2] >= y[2]), item)
    print("Next:", cur, "primary:", primaryLine)
    if len(primaryLine) == 0: continue
    if time-primaryLine[-1][0] > answer: answer = time-primaryLine[-1][0]

# print(steps)
print(answer)
with open("convention2.out", "w") as f: f.write("%s\n" % answer)