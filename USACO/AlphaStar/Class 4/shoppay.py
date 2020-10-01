from queue import Queue
N = int(input())
registers = [list() for _ in range(N)]

waitingLine = Queue()
while True:
    try: process = input()
    except: break
    if not process: break
    process = process.split(" ")
    mode, n = process[0], int(process[1])
    if mode == "C": waitingLine.put(n)
    else:
        if not waitingLine.empty():
            registers[n-1].append(waitingLine.get_nowait())

for r in registers: print(len(r), *r)