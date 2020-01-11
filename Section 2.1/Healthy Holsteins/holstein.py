"""
ID: pranav.19
LANG: PYTHON3
TASK: holstein
"""
V, G = 0, 0
static_required_vitamins = []
feed_types = []

with open("holstein.in", "r") as f:
    V = int(f.readline())
    static_required_vitamins = [int(i) for i in f.readline().split(" ")]
    G = int(f.readline())
    for i in range(G):
        feed_types.append([int(i) for i in f.readline().split(" ")])
#
# print(V)
# print(*static_required_vitamins)
# print(G)
# for i in feed_types:
#     print(*i)
#
# print()
possibilities = []

def diveFurther(remaining_fill, number_scoops, idx, usedRows):
    global possibilities, feed_types
    for i in range(idx+1, G):
        # print("\t" * number_scoops, i)
        # print("\t" * number_scoops, "Subtracting", *remaining_fill)
        # print("\t" * number_scoops, "by",  *(feed_types[i]))
        differences = [remaining_fill[j]-feed_types[i][j] for j in range(V)]

        # print("\t"*number_scoops, "=", *differences)
        for k in differences:
            if k > 0:
                usedRows.append(i)
                diveFurther(differences, number_scoops+1, i, usedRows)
                del usedRows[len(usedRows)-1]
                break
        else:
            usedRows.append(i)
            # print("\t"*number_scoops, "Adding:", [number_scoops, usedRows])
            possibilities.append([number_scoops, usedRows.copy()])
            del usedRows[len(usedRows)-1]

for i in range(-1, V-1):
    # print(i+1)
    diveFurther(static_required_vitamins, 0, i, [])

possibilities.sort()
# for i in possibilities:
    # print(*i)
# print(possibilities)
with open("holstein.out", "w") as f:
    taken = possibilities[0]
    taken[0] += 1
    f.write("%s " % taken[0])
    s = ""
    for i in range(len(taken[1])):
        taken[1][i] += 1
        s += "%s " % taken[1][i]

    s = s[:len(s)-1]+"\n"
    f.write(s)