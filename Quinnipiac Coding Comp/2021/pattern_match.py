def check(grid, pattern, i, j):
    for a in range(i, i+len(pattern)):
        for b in range(j, j+len(pattern[0])):
            # print(f"Comparing: Grid=({a}, {b}), Pattern=({a-i}, {b-j})")
            if grid[a][b] != pattern[a-i][b-j]:
                return 0
    return 1

def solve(grid, pattern):
    count = 0
    for i in range(len(grid)-len(pattern)+1):
        for j in range(len(grid[0])-len(pattern[0])+1):
            count += check(grid, pattern, i, j)
    return count

T = int(input())
for _ in range(T):
    R, C = map(int, input().split(" "))
    grid = [list(map(int, input().split(" "))) for _ in range(R)]
    R0, C0 = map(int, input().split(" "))
    pattern = [list(map(int, input().split(" "))) for _ in range(R0)]
    # print("Testing:")
    # for i in grid:
        # print(*i)
    # for i in pattern:
        # print(*i)

    # print("------")
    print(solve(grid, pattern))