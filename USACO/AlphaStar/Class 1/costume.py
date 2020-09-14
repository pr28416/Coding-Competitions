# Brute force the first cow, ub-search for the second cow, subtract their indices

N, S = map(int, input().split(" "))
cows = sorted([int(input()) for _ in range(N)])

i, j = 0, len(cows)-1
count = 0
while i < j:
    if cows[j]+cows[i] <= S:
        count += j-i
        i += 1
    else: j -= 1
print(count)