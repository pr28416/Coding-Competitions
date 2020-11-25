N, K = map(int, input().split(" "))
adjectives = [set() for _ in range(30)]
nocows = set()
for _ in range(N):
    line = input().split(" ")
    for i in range(4, len(line)-1):
        adjectives[i-4].add(line[i])
    nocows.add(tuple(line[4:len(line)-1]))

adjectives = list(map(sorted, filter(lambda x: len(x) > 0, adjectives)))
# print(adjectives)

def bs(x, lst):
    lo, up = 0, len(lst)
    while lo < up:
        y = (lo+up)//2
        if x == lst[y]: return y
        elif x < lst[y]: up=y
        else: lo=y+1

newParam = set()
for comb in nocows:
    sequence = []
    for i in range(len(comb)):
        sequence.append(bs(comb[i], adjectives[i]))
    newParam.add(tuple(sequence))

combinations = []
k = 1
finComb = []
# print(newParam)
step = 0
def recurse(i, sequence):
    global N, K, adjectives, k, newParam, finComb, step
    if i == len(adjectives):
        print('checkpoint', step)
        step += 1
        if tuple(sequence) in newParam: return False
        if k == K:
            finComb = sequence
            return True
        k += 1
    else:
        for j in range(len(adjectives[i])):
            sequence.append(j)
            if recurse(i+1, sequence):
                return True
            sequence.pop()
    return False


recurse(0, [])


# print(finComb)
final = ""
for i in range(len(finComb)):
    final += adjectives[i][finComb[i]]
    if i != len(finComb)-1: final += " "

print(final)