T = int(input())
for q in range(T):
    N = int(input())
    hills = list(map(int, input().split(" ")))
    c = 0
    for i in range(1, N-1):
        if hills[i] > hills[i-1] and hills[i] > hills[i+1]:
            c += 1
    print(f"Case #{q+1}: {c}")