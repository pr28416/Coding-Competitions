"""
ID: pranav.19
LANG: PYTHON3
TASK: milk2
"""

import sys
sys.setrecursionlimit(100000000)
N = 0
times = []
with open("milk2.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        line = f.readline().split(" ")
        times.append([int(line[0]), int(line[1])])

def split(data):
    if len(data) == 1:
        return data
    else:
        a = split(data[0:int(len(data)/2)])
        b = split(data[int(len(data)/2):len(data)])
        return merge(a, b)

def merge(a, b):
    group = []
    while len(a) > 0 and len(b) > 0:
        if a[0][0] < b[0][0]:
            group.append(a.pop(0))
        else:
            group.append(b.pop(0))
    while len(a) > 0:
        group.append(a.pop(0))
    while len(b) > 0:
        group.append(b.pop(0))
    return group

if N != 0:
    times = split(times)

# print("starting")
startTimes = []
endTimes = []
for i in times:
    startTimes.append(i[0])
    endTimes.append(i[1])
# for i in range(N):
#     print (startTimes[i], endTimes[i])

# Get most idle
idle = 0

    
# Get longest continuous time
# deb = 0
# didHitEnd = False
def getNext(idx, end):
    # print (idx, end)
    for i in range(idx+1, N):
        if startTimes[i] <= end and end <= endTimes[i] and i != idx:
            # print (i)
            return getNext(i, endTimes[i])
    else:
        # deb = end
        return end

# data = [getNext(i, endTimes[i])-startTimes[i] for i in range(int(N))]

data = []

    
    # print("next: %s" % itr)

# print(data)

continuous = 0

def checkNext(i, currentMax):
    if i == N-1:
        return currentMax
    
    temp = 1
    while not(endTimes[i+temp] - endTimes[i] > 0):
        # print(endTimes[i+temp])
        temp += 1
        if i+temp >= N-1:
            return currentMax
    if endTimes[i] < startTimes[i+temp] and startTimes[i+temp] - endTimes[i] > currentMax:
        currentMax = startTimes[i+temp] - endTimes[i]
    
    if i+temp == N-1:
        return currentMax
    return checkNext(i+temp, currentMax)
    

if len(times) != 0:

    # m = 0
    differences = []
    i = 0
    while i < N-1:
        if startTimes[i+1]-endTimes[i] > 0:
            differences.append(startTimes[i+1]-endTimes[i])
        else:
            differences.append(0)
        
        i += 1
    
    # Code for getting longest idle
    i = 0
    idle = checkNext(0, idle)
    # --------------

    # print (differences)
    itr = 0
    while itr < N-1:
        if differences[itr] == 0:
            end = getNext(itr, endTimes[itr])
            data.append(end - startTimes[itr])
            while differences[itr] == 0:
                itr += 1
                if itr == N-1:
                    break
            else:
                continue
            break
        else:
            itr += 1

    if len(data) == 1:
        continuous = data[0]
    elif len(data) == 0:
        continuous = endTimes[0]-startTimes[0]
    else:
        continuous = max(data)
else:
    continuous = 0
    idle = 0
# continuous = getNext(0, endTimes[0])-startTimes[0]
# print("continuous", continuous)


# print ("idle:", idle)
with open("milk2.out", "w") as f:
    f.write("%s %s\n" % (continuous, idle))
