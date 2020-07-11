gameboard = []
with open("tttt.in", "r") as f:
    for i in range(3):
        gameboard.append([i for i in f.readline().strip("\n")])

indivWinners, groupWinners = 0, 0
prevWinners = set()

# Find individual winners
for i in range(3):
    # Row
    if len(set(gameboard[i])) == 1 and gameboard[i][0] not in prevWinners:
        indivWinners += 1
        prevWinners.add(gameboard[i][0])
    # Col
    if gameboard[0][i] == gameboard[1][i] and gameboard[1][i] == gameboard[2][i] and gameboard[0][i] not in prevWinners:
        indivWinners += 1
        prevWinners.add(gameboard[0][i])

# Diag-LR
if len({gameboard[i][i] for i in range(3)}) == 1 and gameboard[1][1] not in prevWinners:
    indivWinners += 1
    prevWinners.add(gameboard[1][1])

# Diag-RL

if len({gameboard[i][2-i] for i in range(3)}) == 1 and gameboard[1][1] not in prevWinners:
    indivWinners += 1
    prevWinners.add(gameboard[1][1])

prevWinners = set()

# Find group winners
e = None
for i in range(3):
    # Row
    e = tuple(sorted(list(set(gameboard[i]))))
    print(e)
    if len(e) == 2 and e not in prevWinners:
        groupWinners += 1
        prevWinners.add(e)

    print("row", i, groupWinners)
    # Col
    e = tuple(sorted(list(set(gameboard[j][i] for j in range(3)))))
    print(e)
    if len(e) == 2 and e not in prevWinners:
        groupWinners += 1
        prevWinners.add(e)

    print("col", i, groupWinners)

# Diag-LR
e = tuple(sorted(list(set([gameboard[i][i] for i in range(3)]))))
print(e)
if len(e) == 2 and e not in prevWinners:
    groupWinners += 1
    prevWinners.add(e)
print("diag-lr", groupWinners)
# Diag-RL

e = tuple(sorted(set(list([gameboard[i][2-i] for i in range(3)]))))
print(e)
if len(e) == 2 and e not in prevWinners:
    groupWinners += 1
    prevWinners.add(gameboard[1][1])

print("diag-rl", groupWinners)
with open("tttt.out", "w") as f:
    f.write("%s\n%s\n" % (indivWinners, groupWinners))