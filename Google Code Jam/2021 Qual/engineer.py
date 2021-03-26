from itertools import permutations as permute

def reverse(lst, i, j):
    for k in range(j-i):
        if i+k > j-k: break
        tmp = lst[i+k]
        lst[i+k] = lst[j-k]
        lst[j-k] = tmp

def reversort(lst):
    cost = 0
    for i in range(len(lst)-1):
        j = i
        for s in range(i, len(lst)):
            if lst[s] < lst[j]: j = s
        reverse(lst, i, j)
        # print(i+1, j+1, lst)
        cost += j-i+1
    return cost

def run():
    T = int(input())
    for t in range(1, T+1):
        N, C = map(int, input().split(" "))
        permutations = list(permute([i for i in range(1, N+1)]))
        # print(permutations)

        for p in permutations:
            i = reversort(list(p))
            if reversort(list(p)) == C:
                # print(i, C, p)
                print(f"Case #{t}:", *p)
                break
        else:
            print(f"Case #{t}: IMPOSSIBLE")

        # print(reversort([1, 2, 3, 4]))
        # print(reversort([1, 2]))
        # print(reversort([1, 2, 3, 4, 5, 6, 7]))

        # print(permutations)

run()