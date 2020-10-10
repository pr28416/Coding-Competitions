with open("convention2.in") as f:
    N = int(f.readline())
    waitingLine = [list(map(int, f.readline().split(" "))) for _ in range(N)]
    for t in range(N):
        waitingLine[t].append(t+1)
        # times[t][1] += times[t][0]

waitingLine.sort(reverse=True, key=lambda x: (x[0], x[2]))
# for i in times: print(i)

# from queue import Queue
# currentQueue = Queue()
time = 0
while len(waitingLine) > 0:
    cur = waitingLine.pop()
    print("Currently looking at:", cur)
    tmp = []
    while len(waitingLine) > 0 and waitingLine[-1][0] < cur[0]+cur[1]:
        tmp.append(waitingLine.pop())
    tmp.sort(reverse=True, key=lambda x: x[2])
    if len(tmp) > 0:
        time += (cur[0]+cur[1])-waitingLine[-1][0]
        tmp[-1][0] = cur[0]+cur[1]
        tmp.pop()
    for i in tmp:
        waitingLine.append(i)

print(time)
