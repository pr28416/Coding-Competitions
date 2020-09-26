N = int(input())
guesses = [tuple(map(int, input().split(" "))) for _ in range(N)]
guesses.sort(key=lambda x: (-x[1], -x[2]))
for i in guesses:
    print(i)

numbers = {i for i in range(10)}

#  x   x   x   x
# ___ ___ ___ ___