from queue import Queue

class Cow:
    def __init__(self, x, y, p):
        self.x = int(x)
        self.y = int(y)
        self.p = int(p)
        self.n = 1
        self.neighbors = []
        self.visited = False
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
        # return "(%s, %s, p:%s, n:%s)" % (self.x, self.y, self.p, self.n)

    def distanceTo(self, other):
        return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5


with open("moocast.in") as f:
    N = int(f.readline())
    cows = [Cow(*f.readline().split(" ")) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j: continue
        if cows[i].distanceTo(cows[j]) <= cows[i].p:
            cows[i].neighbors.append(cows[j])

# print("\nBEFORE\n")
# for i in cows:
#     print(i, 'neighbors:')
#     for n in i.neighbors:
#         print("\t", n)

fin = 0
for cow in cows:
    if cow.visited:
        # print("Skip:", cow)
        continue
    cow.visited = True
    queue = Queue()
    queue.put(cow)
    count = 0
    # print("New:", cow)
    while not queue.empty():
        item = queue.get_nowait()
        # print("\tReach:", item)
        count += 1
        for n in item.neighbors:
            if not n.visited:
                # n.n = item.n+1
                n.visited = True
                queue.put(n)
    fin = max(fin, count)
    for i in cows:
        i.visited = False

# print("\nAFTER\n")
# for i in cows:
#     print(i, 'neighbors:')
#     for n in i.neighbors:
#         print("\t", n)
# print(fin)

with open("moocast.out", "w") as f:
    f.write("%s\n" % fin)