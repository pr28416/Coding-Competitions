from collections import deque
T = int(input())
for _ in range(T):
    encoded = input().strip("\n")
    dq = deque()
    for i in encoded:
        if i == "<" and len(dq) > 0:
            dq.popleft()
        elif i == ">" and len(dq) > 0:
            dq.pop()
        elif 0 <= ord(i)-65 < 26:
            dq.append(i)
    print("".join(list(dq)))