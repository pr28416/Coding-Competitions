with open("cowcode.in") as f:
    s, N = f.readline().split(" ")
    N = int(N)-1

M = len(s)
while M * 2 < N:
    M *= 2

while N >= len(s):
    if N == M: N -= 1
    elif N > M: N -= M + 1
    M //= 2

with open("cowcode.out", "w") as f:
    f.write("%s\n" % s[N])