N, L = 0, 0
points = [list(map(int, input().split(" "))) for _ in range(N)]
points.sort(key=lambda x: x[1])