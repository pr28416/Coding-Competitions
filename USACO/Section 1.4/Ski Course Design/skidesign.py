"""
ID: pranav.19
LANG: PYTHON3
TASK: skidesign
"""
N = 0
hills = []

with open("skidesign.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        hills.append(int(f.readline()))

print(N, hills)

def split(n):
    if len(n) == 1:
        return n
    else:
        a = split(n[:int(len(n)/2)])
        b = split(n[int(len(n)/2):])
        return merge(a, b)

def merge(a, b):
    n = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            n.append(a.pop(0))
        else:
            n.append(b.pop(0))
    while len(a) > 0:
        n.append(a.pop(0));
    while len(b) > 0:
        n.append(b.pop(0))
        
    return n

hills = split(hills)
print(hills)
totalCost = 0

canChange = True
toggle = True
if len(hills) == 1:
    if hills[0] > 17:
        totalCost = (hills[0]-17)**2
else:
    while  hills[len(hills)-1]-hills[0] > 17:
        # Keep changing bottom value
        canChange = False
        temp = 0
        if toggle:
            # Changing the first
            while hills[len(hills)-1]-hills[0] > 17 and hills[0] < hills[1]:
                hills[0] += 1
                temp += 1
                canChange = True
            totalCost += temp**2
        else:
            # Changing the end
            while hills[len(hills)-1]-hills[0] > 17 and hills[len(hills)-1] > hills[len(hills)-2]:
                hills[len(hills)-1] -= 1
                temp += 1
                canChange = True
            totalCost += temp**2
        
        hills = split(hills)
        toggle = not toggle
        print(hills)


print(totalCost)
with open("skidesign.out", "w") as f:
    f.write("{}\n".format(totalCost))