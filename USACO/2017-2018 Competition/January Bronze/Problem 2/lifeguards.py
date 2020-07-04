N = 0
times = []

with open("lifeguards.in", "r") as f:
    N = int(f.readline())
    temp = []
    for i in range(N):
        temp.append([int(j) for j in f.readline().split(" ")])

    def merge(a, b):
        x = []
        while len(a) > 0 and len(b) > 0:
            if a[0][0] < b[0][0]:
                x.append(a.pop(0))
            elif a[0][0] > b[0][0]:
                x.append(b.pop(0))
            else:
                x.append(a.pop(0) if a[0][1] < b[0][1] else b.pop(0))
        while len(a) > 0: x.append(a.pop(0))
        while len(b) > 0: x.append(b.pop(0))
        return x
    
    def split(x):
        if len(x) == 1:
            return x
            
        a = split(x[:len(x)//2])
        b = split(x[len(x)//2:])
        return merge(a, b)
    
    times = split(temp)

maxTime = 0

for i in range(len(times)):
    remaining = [[*i] for i in [*times[:i], *times[i+1:]]]
    # print("original times:", *times)
    # print("\tpre-condensed:", *remaining)
    # Condense
    for j in range(len(remaining)-1, 0, -1):
        if remaining[j][0] <= remaining[j-1][1]:
            remaining[j-1][1] = remaining[j][1]
            del remaining[j]
    
    # print("\tcondensed:", *remaining, "\n")

    # Count
    count = 0
    for j in remaining:
        count += j[1] - j[0]
    maxTime = count if count > maxTime else maxTime

# print(maxTime)
with open("lifeguards.out", "w") as f:
    f.write("%s\n" % maxTime)