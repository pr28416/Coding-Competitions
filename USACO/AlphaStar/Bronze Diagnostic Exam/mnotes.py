N, Q = map(int, input().split(" "))
notes = []
# [int(input()) for i in range(N)]
prev = 0
for i in range(N):
    next = int(input())
    notes.append([prev, prev + next])
    prev += next

queries = [int(input()) for i in range(Q)]
answers = []

for query in queries:
    lo, up = 0, len(notes)
    while lo <= up:
        y = lo + (up - lo) // 2
        # Found index
        if query >= notes[y][0] and query < notes[y][1]:
            answers.append(y+1)
            break
        # < index
        elif query < notes[y][0]:
            up = y - 1
        # > index
        else:
            lo = y + 1

for i in answers:
    print(i)
