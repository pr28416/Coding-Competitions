N = int(input())
pairs = []
for _ in range(N):
    pairs.append(input().split(" ") + [1])

pairs.sort()
# print(pairs)

def bs(lst, x, comp):
    lo, up = 0, len(lst)
    while lo < up:
        y = lo + (up-lo) // 2
        if comp(x, lst[y][0][:2]): up = y
        else: lo = y+1
    return lo

answers = set()
for i in pairs:
    sub = pairs[bs(pairs, i[1], lambda x, y: x <= y):bs(pairs, i[1], lambda x, y: x < y)]
    # print(i)
    # print('\tpulled in:', sub)
    for s in sub:
        if s[2] and i[1] == s[0][:2] and i[0][:2] == s[1]:
            answers.add(tuple(sorted([i[0], s[0]])))
            i[2], s[2] = 0, 0

# print(answers)
print(len(answers))