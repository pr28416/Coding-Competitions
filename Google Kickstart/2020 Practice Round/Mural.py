def solve(T, N, sections):
    sums = [0] * (N+1)
    for i in range(1, N+1):
        sums[i] = sums[i-1] + sections[i]

    k = (N+1)//2
    maxSum = 0

    for i in range(k, N+1):
        if sums[i]-sums[i-k] > maxSum: maxSum = sums[i]-sums[i-k]

    print(f"Case #{T}: {maxSum}")

for T in range(int(input())):
    solve(T+1, int(input()), [0] + [int(i) for i in input()])