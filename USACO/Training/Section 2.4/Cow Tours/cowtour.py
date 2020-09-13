"""
ID: pranav.19
LANG: PYTHON3
TASK: cowtour
"""

class Node:
    def __init__(self, x, y):
        self.x, self.y, self.neighbors, self.diameter = x, y, [], 0
    def addNeighbor(self, node): self.neighbors.append(node)
    def distanceTo(self, other): return ((self.x-other.x)**2+(self.y-other.y)**2)**0.5
    def __str__(self): return f"({self.x},{self.y})"
    def __repr__(self): return self.__str__()

N = nodes = matrix = distances = None
with open("cowtour.in", "r") as f:
    N = int(f.readline())
    nodes = [Node(*map(int, f.readline().strip("\n").split(" "))) for _ in range(N)]
    matrix = [list(map(int, list(f.readline().strip("\n")))) for _ in range(N)]
    distances = [[nodes[i].distanceTo(nodes[j]) if matrix[i][j] else None for j in range(N)] for i in range(N)]

print(N)
print(*nodes)
for i in matrix:
    print(*i)

print("distances:")
for i in distances:
    print(*i)

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            nodes[i].addNeighbor(nodes[j])

# for node in nodes:
#     print(f"{node}:", *node.neighbors)

def smallestPath(index):
    global matrix, distances
    paths = [None] * len(matrix) + [150000]
    remaining = {i for i in range(len(matrix))}
    # Finalize at index
    paths[index], last = 0, index
    remaining.discard(index)
    j = 0
    while True:
        smallest = len(paths)-1
        for i in remaining:
            if matrix[last][i] and (paths[i] is None or paths[last] + distances[last][i] < paths[i]):
                paths[i] = paths[last] + distances[last][i]
            if paths[i] is not None and paths[i] < paths[smallest]:
                smallest = i
        # Finalize smallest
        b = len(remaining)
        last = smallest
        remaining.discard(smallest)
        if len(remaining) == 0 or b == len(remaining) or j == len(paths):
            paths[index] = None
            del paths[-1]
            return paths
        j += 1

shortestPaths = []
print("\nSHORTEST PATHS:")
for i in range(len(nodes)):
    shortestPaths.append(smallestPath(i))
    print(f"Shortest paths from {i}: ", *map(lambda x: "%.4f, " % x if x else "None, ", shortestPaths[i]))
groups = []
temp = {0, *(i for i in range(len(shortestPaths[0])) if shortestPaths[0][i])}

for i in range(1, len(shortestPaths)):
    if i not in temp:
        groups.append(tuple(temp))
        temp = {i, *(j for j in range(len(shortestPaths[i])) if shortestPaths[i][j])}

groups.append(tuple(temp))
del temp, shortestPaths
print(*groups)