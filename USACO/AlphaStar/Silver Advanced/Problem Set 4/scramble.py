N = int(input())
cows = [(input(), i) for i in range(N)]

forward = sorted(map(lambda x: ("".join(sorted(x[0])), x[1]), cows))
for i in range(N): forward[i] = (*forward[i], i+1)
forward.sort(key=lambda x: x[1])

backward = sorted(map(lambda x: ("".join(sorted(x[0], reverse=True)), x[1]), cows))
for i in range(N): backward[i] = (*backward[i], i+1)
backward.sort(key=lambda x: x[1])

for i in range(N):
    print(forward[i][2], backward[i][2])