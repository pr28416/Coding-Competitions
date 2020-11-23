from bisect import bisect_left as bsl, bisect_right as bsr

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

    answers[i][0] = bsl(backward, ascending)
    answers[i][1] = bsr(forward, descending)-1

for i in answers: print(i[0]+1, i[1]+1)