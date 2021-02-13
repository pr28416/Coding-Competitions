T = int(input())
for t in range(1, T+1):
    N, D = map(int, input().split(" "))
    for i in map(int, reversed(input().split(" "))):
        D = D // i * i
    print(f"Case #{t}: {D}")