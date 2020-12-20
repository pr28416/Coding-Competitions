from queue import Queue

with open("milkvisits.in") as f:
    N, M = map(int, f.readline().split(" "))
    cowTypes = list(map(lambda x: int(x == 'H'), f.readline().strip("\n")))
    neighbors = [[] for _ in range(N)]
    for _ in range(N-1):
        line = list(map(int, f.readline().split(" ")))
        neighbors[line[0]-1].append(line[1]-1)
        neighbors[line[1]-1].append(line[0]-1)
    queries = [f.readline().strip("\n").split(" ") for _ in range(M)]

# print(cowTypes)
# for i in neighbors:
#     # print(i)

visited = [0] * N
binary = ["0"] * M

components = [set()]
mapped = {}

for i in range(len(visited)):
    if visited[i]:
        continue
    queue = Queue()
    queue.put_nowait(i)
    visited[i] = 1

    while not queue.empty():
        item = queue.get_nowait()
        components[-1].add(item)
        mapped[item] = len(components)-1
        for n in neighbors[item]:
            if not visited[n] and cowTypes[n] == cowTypes[i]:
                visited[n] = 1
                queue.put_nowait(n)

    components.append(set())

components.pop()

# print(components)
# print(mapped)
for i, query in enumerate(queries):
    start, end = int(query[0])-1, int(query[1])-1
    milkType = int(query[2] == 'H')
    if mapped[start] != mapped[end]:
        binary[i] = "1"
    else:
        binary[i] = str(int(cowTypes[start] == milkType))

# for i, query in enumerate(queries):
#     # print(query)
#     visited = [0] * N
#     start, end = int(query[0])-1, int(query[1])-1
#     milkType = int(query[2] == 'H')
#     # print('going from', start, 'to', end, '%s %s %s' % (milkType, cowTypes[start], cowTypes[end]))
#     if cowTypes[start] == milkType or cowTypes[end] == milkType:
#         # print('skip')
#         binary[i] = "1"
#         continue
    
#     queue = Queue()
#     queue.put_nowait((start, 0))
#     visited[start] = 1

#     while not queue.empty():
#         item = queue.get_nowait()
#         # print(item)
#         if item[0] == end:
#             binary[i] = str(item[1])
#             break
        
#         for n in neighbors[item[0]]:
#             if not visited[n]:
#                 e = max(item[1], int(cowTypes[item[0]] == milkType))
#                 visited[n] = 1
#                 queue.put_nowait((n, e))

# print("".join(binary))
with open("milkvisits.out", "w") as f:
    f.write("%s\n" % "".join(binary))