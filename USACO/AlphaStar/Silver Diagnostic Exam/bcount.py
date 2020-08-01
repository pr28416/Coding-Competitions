N, Q = map(int, input().split(" "))
cowBreeds = [int(input()) for i in range(N)]
queries = [list(map(int, input().split(" "))) for i in range(Q)]
for i in range(len(queries)):
    queries[i].append(i)

queries.sort(key=lambda x: x[0])

# print(N, Q)
# print(cowBreeds)
# print(queries)

# for query in queries:
#     a, b = query[0]-1, query[1]
#     breedCount = [0] * 3 # [Holsteins, Guernseys, Jerseys]
#     for i in range(a, b):
#         breedCount[cowBreeds[i]-1] += 1
#     print(*breedCount)

prev = [1, N]
breedCount = [0] * 3
answers = []
for i in cowBreeds:
    breedCount[i-1] += 1
for query in range(len(queries)):
    # Modify lower bound
    for i in range(prev[0]-1, queries[query][0]-1):
        breedCount[cowBreeds[i]-1] -= 1
    # Modify upper bound
    if prev[1] < queries[query][1]:
        for i in range(prev[1], queries[query][1]):
            breedCount[cowBreeds[i]-1] += 1
    elif prev[1] > queries[query][1]:
        for i in range(prev[1]-1, queries[query][1]-1, -1):
            breedCount[cowBreeds[i]-1] -= 1
    answers.append([*breedCount, queries[query][2]])
    # print(*breedCount)
    prev = queries[query]

answers.sort(key=lambda x: x[3])
for i in answers:
    print(*i[:3])

# [2, 1, 1, 3, 2, 1]
# [1, 6] to [2, 4]
