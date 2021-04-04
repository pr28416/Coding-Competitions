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
        N = int(input())
        print(f"Case #{t}: {reversort(list(map(int, input().split(' '))))}")

def test():
    lst = [1, 2, 3, 4, 5, 6]
    reverse(lst, 1, 4)
    print(lst)

run()