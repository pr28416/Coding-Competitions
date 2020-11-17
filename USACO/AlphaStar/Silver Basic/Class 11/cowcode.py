word, N = input().split(" ")
N = int(N)-1
M = len(word)
while M <= N: M *= 2
while M > len(word):
    if N > M//2: N = (N-M//2-1) % (M//2)
    elif N == M//2: N = (N-1) % (M//2)
    M //= 2
print(word[N])