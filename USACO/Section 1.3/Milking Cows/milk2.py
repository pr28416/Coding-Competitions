"""
ID: pranav.19
LANG: PYTHON3
TASK: milk2
"""
N = 0
start = []
end = []
with open("milk2.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        line = f.readline().split(" ")
        start.append(int(line[0]))
        end.append(int(line[1]))

swap = True
while swap == True:
    swap = False
    for i in range(N-1):
        if start[i] > start[i+1]:
            start[i], start[i+1] = start[i+1], start[i]
            end[i], end[i+1] = end[i+1], end[i]
            swap = True

for i in range(N):
    print (start[i], end[i])

print("Initiating")

def getLongest(idx, smallest, largest):
    if idx >= N-1:
        return largest-smallest
    else:
        if largest >= start[idx+1] and largest <= end[idx]:
            largest = end[idx+1]
        
        return getLongest(idx+1, smallest, largest)

def getSmallest(idx, smallest):
    print(smallest)
    if idx >= N-1:
        return smallest
    else:
        if start[idx+1]-end[idx] > 0 and start[idx+1]-end[idx] < smallest:
            smallest = start[idx+1]-end[idx]

        return getSmallest(idx+1, smallest)

if N != 0:
    longest = getLongest(0, start[0], end[0])
    smallest = 0
    if longest < max(end) - min(start):
        smallest = getSmallest(0, max(end) - min(start))
    print("Final: %s %s" % (longest, smallest))
else:
    print("Final: %s %s" % (0, 0))