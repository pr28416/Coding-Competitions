from collections import deque
qu = deque()
S = int(input())
i = 1
for _ in range(S):
    command = input().split(" ")
    if command[0] == "A":
        if command[1] == "L":
            qu.appendleft(i)
        else:
            qu.append(i)
        i += 1
    else:
        for _ in range(int(command[2])):
            if command[1] == "L":
                qu.popleft()
            else: qu.pop()
for i in qu:
    print(i)