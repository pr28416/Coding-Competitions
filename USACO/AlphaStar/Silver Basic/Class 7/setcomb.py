M = int(input())
nums = input().split(" ")
N = int(input())

def recurse(c, used, k, j):
    global nums, N, M
    if c == k:
        print("".join(nums[i] for i in range(M) if used[i]))
    else:
        for i in range(j, M):
            used[i] = 1
            recurse(c+1, used, k, i+1)
            used[i] = 0

recurse(0, [0] * M, N, 0)