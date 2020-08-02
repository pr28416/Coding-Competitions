N = int(input())
elsieCards = []
elsieCards = [int(input()) for i in range(N)]
elsieCards.sort(reverse=True)

bessieCards = []
eIdx = 0
for b in range(2*N, 0, -1):
    if eIdx == N and b < elsieCards[N-1]:
        bessieCards.append(b)
        continue
    if elsieCards[eIdx] == b:
        eIdx += 1
        continue
    if elsieCards[eIdx] < b:
        bessieCards.append(b)
        continue

wins = 0
bIdx = 0
for e in elsieCards:
    if bIdx == N: break
    if bessieCards[bIdx] < e: continue
    wins += 1
    bIdx += 1

print(wins)
