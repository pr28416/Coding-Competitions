N = int(input())
notes = [int(input()) for _ in range(N)]
C = int(input())
tmp = sorted([int(input()) for _ in range(C)])
rumDelta = [tmp[i+1]-tmp[i] for i in range(len(tmp)-1)]

bads = []
for i in range(N-C+1):
    tmp = sorted(notes[i:i+C])
    delta = [tmp[i+1]-tmp[i] for i in range(len(tmp)-1)]
    if delta == rumDelta: bads.append(i)

print(len(bads))
for i in bads: print(i+1)