# N --> number of constraints
N = 0
constraints = []
newGroups = []
final = []
unusedCows = ["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue", "Betsy", "Sue"]
# unusedCows = ["A", "B", "C", "D", "E", "F", "G", "H"]

with open("lineup.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        constraints.append(f.readline().split(" must be milked beside "))

for i in range(len(constraints)):
    constraints[i][0], constraints[i][1] = constraints[i][0].rstrip(), constraints[i][1].rstrip()

# 1st iteration: Sort based on internal values
for c in range(len(constraints)):
    constraints[c].sort()

print(constraints)

# 2nd iteration: Sort based on external values
def split(x):
    if len(x) == 1:
        return x
    a = split(x[:int(len(x)/2)])
    b = split(x[int(len(x)/ 2):])
    return merge(a, b)

def merge(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][0] < b[0][0]:
            x.append(a.pop(0))
        elif a[0][0] > b[0][0]:
            x.append(b.pop(0))
        else:
            if a[0][1] < b[0][1]:
                x.append(a.pop(0))
            else:
                x.append(b.pop(0))
    while len(a) > 0: x.append(a.pop(0))
    while len(b) > 0: x.append(b.pop(0))
    return x

constraints = split(constraints)
print(constraints)

# N-long iteration: Check to make sure that an intersection wasn't performed

def intersect(l1, l2):
    a = [p for p in l1 if p in l2]
    return a

last = constraints[len(constraints)-1]
x = []
didIntersection = True
while didIntersection:
    didIntersection = False
    tempConstraints = constraints.copy()
    print("\n------\nstart with", constraints)
    for i in range(len(constraints)-1):
        # Get intersection of ith constraint and (i+1)th constraint
        print()
        intersection = intersect(constraints[i], constraints[i+1])
        print("intersection", constraints[i], constraints[i+1], "-->", intersection)
        if len(intersection) > 0:
            didIntersection = True
            t1 = [q for q in constraints[i] if q not in intersection]
            t2 = [q for q in constraints[i+1] if q not in intersection]
            # t1.reverse()
            # t2.reverse()
            c = []
            print("t1", t1, "t2", t2)
            if t1 == t2:
                for t1i in t1:
                    c.append(t1i)
            # elif len(t1) == 0:
            #     # for a in intersection:
            #     #     c.append(a)
            #     # for t2i in t2:
            #     #     c.append(t2i)
            #     for y in constraints[i+1]:
            #         c.append(y)
            # elif len(t2) == 0:
            #     # for a in intersection:
            #     #     c.append(a)
            #     # for t1i in t1:
            #     #     c.append(t1i)
            #     for y in constraints[i]:
            #         c.append(y)

            elif t1[len(t1)-1] < t2[len(t2)-1]:
                print(t1[len(t1)-1], "<", t2[len(t2)-1])
                for t1i in t1:
                    c.append(t1i)
                for a in intersection:
                    c.append(a)
                for t2i in t2:
                    c.append(t2i)
            elif t1[len(t1)-1] > t2[len(t2)-1]:
                print(t1[len(t1)-1], ">", t2[len(t2) - 1])
                for t2i in t2:
                    c.append(t2i)
                for a in intersection:
                    c.append(a)
                for t1i in t1:
                    c.append(t1i)
            print("made into", c)
            # tempConstraints.append(c)
            tempConstraints[i+1] = c
            tempConstraints[i] = []
        # else:
            # print("No intersection up there")
            # if not didIntersection:
            #     print("previously no intersection so adding", constraints[i])
            #     tempConstraints.append(constraints[i])

            # print("adding", constraints[i])
            # tempConstraints.append(constraints[i])
    # tempConstraints.append(constraints[len(constraints)-1])
    if didIntersection:
        xy = [j for j in tempConstraints if len(j) > 0]
        constraints = xy.copy()
        print("new", constraints)

# print(constraints)
while [] in constraints:
    del constraints[constraints.index([])]

# Add the remaining cows
for a in constraints:
    for b in a:
        if b in unusedCows:
            unusedCows[unusedCows.index(b)] = None
unusedCows = [i for i in unusedCows if i != None]
for cow in unusedCows:
    for groupIdx in range(len(constraints)):
        if cow < constraints[groupIdx][0]:
            constraints.insert(groupIdx, [cow])
            break
    else:
        constraints.append([cow])

print("Final", constraints)

# Finally, write to the lineup.out file
with open("lineup.out", "w") as f:
    for group in constraints:
        for cow in group:
            f.write("%s\n" % cow)