N = 0 # number of measurements
measures = []
with open("measurement.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        temp = f.readline().split(" ")
        measures.append([int(temp[0]), temp[1], int(temp[2])])

def merge(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][0] < b[0][0]:
            x.append(a.pop(0))
        else:
            x.append(b.pop(0))
    while len(a) > 0:
        x.append(a.pop(0))
    while len(b) > 0:
        x.append(b.pop(0))
    return x

def split(x):
    if len(x) == 1:
        return x
    a = split(x[:len(x)//2])
    b = split(x[len(x)//2:])
    return merge(a, b)

measures = [i[1:] for i in split(measures)]

#-----------
cows = {i[0]:7 for i in measures}
maxOutput = None
count = 0

# for i in measures: print(*i)

def getMax(d):
    global measures
    m = measures[0][0]
    for i in d:
        if d[i] > d[m]:
            m = i
    s = {m}
    for i in d:
        if d[i] == d[m]:
            s.add(i)
    return s

for row in measures:
    cows[row[0]] += row[1]
    if maxOutput == None:
        maxOutput = getMax(cows)
        count += 1
        # print("Display changed:", maxOutput)
    else:
        c = getMax(cows)
        if not (maxOutput - c == set() and c - maxOutput == set()):
            maxOutput = c
            count += 1
            # print("Display changed:", maxOutput)

# for k, v in cows.items():
#     print(k, v)

with open("measurement.out", "w") as f:
    f.write("%s\n" % count)