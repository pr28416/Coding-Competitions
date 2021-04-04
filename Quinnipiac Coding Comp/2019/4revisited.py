T = int(input())
for t in range(T):
    used = {0}
    line = list(map(int, input().split(" ")))
    line.pop(0)
    i = s = 0
    while True:
        s += line[i]
        # print(s, used)
        if s in used: break
        used.add(s)
        i = (i+1) % len(line)
    print(s)

