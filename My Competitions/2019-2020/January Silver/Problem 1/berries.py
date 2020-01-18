N, K = 0, 0
orig = []
trees = []
with open("berries.in", "r") as f:
    t = f.readline().split(" ")
    N = int(t[0])
    K = int(t[1])
    orig = [int(i) for i in f.readline().split(" ")]
    
    orig.sort()
    orig.reverse()
    trees = [[int(i)] for i in orig]

# print(N, K)
# print(*trees)
# print("Start")

answers = []

def getRemovedRep(curTrees, rep):
    c = []
    for i in curTrees:
        t = []
        for j in i:
            t.append(j)
        c.append(t)

    for i in range(len(c)):

        for j in range(len(c[i])):

            if c[i][j] > rep:
                c[i].append(c[i][j]-rep)
                c[i][j] = rep
                break
                
    return c

for rep in orig:
    # Recurse until removedReps are the same
    d = trees.copy()

    while True:
        if d == getRemovedRep(d, rep):
            # Get the entire collection to find the max
            # print("Using", d)
            e = []
            for i in d:
                for j in i:
                    e.append(j)
            e.sort()
            e.reverse()
            # Repeat K times (for each basket) to find max berries
            bessie = []
            # elsie = []
            for i in range(K//2):
                e.pop(0)
            for i in range(K//2):
                bessie.append(e.pop(0))

            # print(sum(bessie))
            answers.append(sum(bessie))
            break

        # Get the entire collection to find the max
        # print("Using", d)
        e = []
        for i in d:
            for j in i:
                e.append(j)
        e.sort()
        e.reverse()
        # Repeat K times (for each basket) to find max berries
        bessie = []
        # elsie = []
        for i in range(K//2):
            e.pop(0)
        for i in range(K//2):
            bessie.append(e.pop(0))

        # print(sum(bessie))
        answers.append(sum(bessie))
        d = getRemovedRep(d, rep)
        # print("new d will be:", d)
    
# print(max(answers))
# print("Done")
with open("berries.out", "w") as f:
    f.write("%s\n" % max(answers))