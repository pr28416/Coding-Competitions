N = int(input())
commands = [input() for _ in range(N)]
stack = []
haybale = 1

for command in commands:
    if command == "ADD":
        stack.append(haybale)
        haybale += 1
    else:
        stack.pop()

print(len(stack))
for i in stack: print(i)