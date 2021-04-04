def solve(V):
    fib = [1, 1]
    while fib[-1] < V:
        fib.append(fib[-1]+fib[-2])
    fib.pop()
    v = V
    nums = []
    print(fib)
    i = len(fib)-1
    while v > 0 and i >= 0:
        if not fib[i] > v:
            nums.append(fib[i])
            v -= fib[i]
        i -= 1
    return nums[::-1]

T = int(input())
for _ in range(T):
    print(*solve(int(input())))