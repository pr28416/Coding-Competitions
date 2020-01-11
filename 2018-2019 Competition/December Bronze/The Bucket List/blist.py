N = 0
sVals = []
tVals = []
bVals = []

class Bucket:
    isBeingUsed = False
    hasBeenUsedBefore = False
    s = 0
    t = 0

buckets = [Bucket() for i in range(1000)]

with open("blist.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        temp = f.readline().split(" ")
        sVals.append(int(temp[0]))
        tVals.append(int(temp[1]))
        bVals.append(int(temp[2]))

swap = True
while swap:
    swap = False
    for i in range(N-1):
        if sVals[i] > sVals[i+1]:
            sVals[i], sVals[i+1] = sVals[i+1], sVals[i]
            tVals[i], tVals[i+1] = tVals[i+1], tVals[i]
            bVals[i], bVals[i+1] = bVals[i+1], bVals[i]
            swap = True

# for i in range(N):
#     print(sVals[i], tVals[i], bVals[i])

# First get the end time for all milking
ENDING_TIME = max(tVals)

# Function for updating which buckets are being used
def updateModel(interval):
    for i in buckets:
        if i.t < interval:
            i.isBeingUsed = False

# Function for getting first unused bucket
def getAvailableBucket():
    for i in range(len(buckets)):
        if buckets[i].isBeingUsed == False:
            return i

# Start progressing through all the times
for i in range(1, ENDING_TIME+1):
    # print("Time is now: %s" % i)
    updateModel(i)
    # printAll()

    if i in sVals:
        # Get the index of this -- idx is now what we will check what buckets to use.
        idx = sVals.index(i)

        # Check off the buckets we need for idx

        for j in range(bVals[idx]): # Repeating j times, where j is the number of buckets needed
            g = getAvailableBucket()
            # print("Assigning bucket:", g)
            buckets[g].isBeingUsed = True
            buckets[g].s = sVals[idx]
            buckets[g].t = tVals[idx]
            buckets[g].hasBeenUsedBefore = True

# Run through all buckets to see which have been used before

counter = 0
for i in range(len(buckets)):
    if buckets[i].hasBeenUsedBefore:
        # print("FINAL -- Has been used:", i)
        counter += 1

# print(counter)
with open("blist.out", "w") as f:
    f.write("%s\n" % counter)