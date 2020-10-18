M = int(input())
nums = input().split(" ")
N = int(input())

def recurse(s, k):
    global nums
    if len(s) == k: print(s)
    else:
        for i in nums: recurse(s+i, k)

recurse("", N)