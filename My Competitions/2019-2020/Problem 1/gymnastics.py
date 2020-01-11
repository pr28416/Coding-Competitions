# K: num practice sessions, N: num cows
N, K = 0, 0
sessions = []

with open("gymnastics.in", "r") as f:
    temp = f.readline().split(" ")
    K, N = int(temp[0]), int(temp[1])
    for i in range(K):
        sessions.append([int(i) for i in f.readline().split(" ")])

numConsistentPairs = []

# Get pair from first session
for i, a in enumerate(sessions[0]):
    for b in sessions[0][i+1:]:
        # Iterate through each session, Check if A more consistent than B
        for session in range(1, len(sessions)):
            # print(b, sessions[session][sessions[session].index(a):])
            if b not in sessions[session][sessions[session].index(a):]:
                break
        else:
            pair = [a, b]
            pair.sort()
            if pair not in numConsistentPairs: numConsistentPairs.append(pair)

# print(len(numConsistentPairs), numConsistentPairs)
with open("gymnastics.out", "w") as f:
    f.write("%s\n" % len(numConsistentPairs))