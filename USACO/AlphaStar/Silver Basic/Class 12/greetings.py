B, E = map(int, input().split(" "))

bMoves = [0]
for _ in range(B):
    e = input().split(" ")
    for _ in range(int(e[0])):
        bMoves.append(bMoves[-1]+(1 if e[1] == "R" else -1))
    # bMoves.append(int(e[0]) * (1 if e[1] == "R" else -1))

eMoves = [0]
for _ in range(E):
    e = input().split(" ")
    for _ in range(int(e[0])):
        eMoves.append(eMoves[-1]+(1 if e[1] == "R" else -1))

# print(bMoves)
# print(eMoves)

count = 0
for i in range(1, max(len(bMoves), len(eMoves))):
    bIdx, eIdx = min(i, len(bMoves)-1), min(i, len(eMoves)-1)
    # print(bMoves[bIdx], eMoves[eIdx], "\t", bIdx, eIdx)
    if bMoves[bIdx] == eMoves[eIdx] and bMoves[min(i-1, bIdx)] != eMoves[min(i-1, eIdx)]:
        # print(max(bIdx, eIdx))
        # print("Meetpoint")
        count += 1

print(count)