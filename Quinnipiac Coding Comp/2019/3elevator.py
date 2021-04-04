def solve(k, places):
    return sum(places)

T = int(input())
for t in range(T):
    line = list(map(int, input().split(" ")))
    print(solve(line[0], line[1:]))