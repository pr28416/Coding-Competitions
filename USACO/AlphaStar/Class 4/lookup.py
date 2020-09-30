N = int(input())
cows = [int(input()) for _ in range(N)]
table, stack = [], []
for i in range(len(cows)-1, -1, -1):
    while len(stack) > 0 and cows[stack[-1]] <= cows[i]: stack.pop()
    if len(stack) == 0: table.append(0)
    else: table.append(stack[-1]+1)
    stack.append(i)
for i in range(len(table)-1, -1, -1): print(table[i])