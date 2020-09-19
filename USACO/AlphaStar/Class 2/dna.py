M, F = map(int, input().split(" "))
animals = [input() for _ in range(M+F)]
grid = [[0] * F for _ in range(M)]

# print("Before")
# for i in animals: print(i)

# Remove unimportant part of DNA from front and back
st = 0
for i in range(25):
    if len(set(map(lambda x: x[i], animals))) <= 1: st += 1
    else: break

en = 25
for i in range(24, -1, -1):
    if len(set(map(lambda x: x[i], animals))) <= 1: en -= 1
    else: break

# print(st, en)
animals = list(map(lambda x: "x"+x[st:en], animals))

# print("After")
# for i in animals: print(i)

# Check for children

def isChild(p1, p2, child):
    for i in range(len(child)):
        if child[i] != p1[i] and child[i] != p2[i]:
            return False
    return True

for m in range(M):
    for f in range(F):
        for c in range(M+F):
            if c == m or c == f+M: continue
            if isChild(animals[m], animals[f+M], animals[c]):
                grid[m][f] += 1

for i in grid:
    print(*i)