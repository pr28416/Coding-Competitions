M = int(input())
nums = input().split(" ")
N = int(input())

def recurse(s, k, used):
    global nums
    if len(s) == k: print(s)
    else:
        for i in range(len(used)):
            if used[i]: continue
            used[i] = 1
            recurse(s+nums[i], k, used)
            used[i] = 0

recurse("", N, [0]*M)