def solve(T, N, K, A):
    fin = 0
    for i in range(1, K+1):
        finsub = 0
        for s in range(N):
            sub = 0
            # print("Starting at", A[s])
            for p in range(s, N):
                # print("\tAdding", A[p])
                sub += A[p] * (p-s+1)**i
                finsub += sub
        fin += finsub
    print(f"Case #{T}: {fin % (10**9+7)}")

for T in range(int(input())):
    N, K, x1, y1, C, D, E1, E2, F = map(int, input().split(" "))
    array = [0] * N
    xi, yi = x1, y1
    for i in range(N):
        array[i] = (xi+yi)%F
        xi, yi = (C*xi+D*yi+E1)%F, (D*xi+C*yi+E2)%F
    solve(T+1, N, K, array)