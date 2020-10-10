N = int(input())
matrix = [list(map(int, input().split(" "))) for _ in range(N)]

largest = None

# Horizontal
for i in range(N):
    a = None
    for j in range(N):
        b = 0
        for k in range(N):
            b += matrix[i][(j+k)%N]
            if a is None or b > a: a = b
    if largest is None or a > largest: largest = a

# Vertical
for i in range(N):
    a = None
    for j in range(N):
        b = 0
        for k in range(N):
            b += matrix[(j+k)%N][i]
            if a is None or b > a: a = b
    if a > largest: largest = a

# L-Diagonal
for i in range(N):
    a = None
    for j in range(N):
        b = 0
        for k in range(N):
            b += matrix[(i+j+k)%N][(j+k)%N]
            if a is None or b > a: a = b
    if a > largest: largest = a

# R-Diagonal
for i in range(N):
    a = None
    for j in range(N):
        b = 0
        for k in range(N):
            b += matrix[(i-j-k)%N][(j+k)%N]
            if a is None or b > a: a = b
    if a > largest: largest = a

print(largest)