def bs(x, lst, comp):
    lo, up = 0, len(lst)
    while lo < up:
        y = (lo+up)//2
        if comp(x, lst[y]): up=y
        else: lo=y+1
    return lo

N = int(input())
original = [input() for i in range(N)]
answers = [[0, 0] for _ in range(N)]

forward = sorted(map(
    lambda x: "".join(sorted(x)),
    original))
backward = sorted(map(
    lambda x: "".join(sorted(x, reverse=True)),
    original))

for i in range(N):
    ascending = "".join(sorted(original[i]))
    descending = "".join(sorted(original[i], reverse=True))

    # Search ascending in backward - best loc
    loc = bs(ascending, backward, lambda x, y: x <= y)
    answers[i][0] = loc

    # Search descending in forward - worst loc
    loc = bs(descending, forward, lambda x, y: x < y)
    answers[i][1] = loc-1

for i in answers:
    print(i[0]+1, i[1]+1)