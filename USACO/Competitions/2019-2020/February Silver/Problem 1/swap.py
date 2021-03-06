# N: number of cows
# M: number of pairs of integers (swaps)
# K: Repetitions of the M-step process
N, M, K = 0, 0, 0
moves = []
cows = []

with open("swap.in", "r") as f:
    temp = f.readline().split(" ")
    N, M, K = int(temp[0]), int(temp[1]), int(temp[2])
    cows = [i+1 for i in range(N)]
    for i in range(M):
        temp = f.readline().split(" ")
        moves.append([int(i) for i in temp])
# print("k: st, move: st ==> %s" % (cows))


for k in range(K):
    for move in moves:
        # print("Adding %s + %s + %s ||| bounds for second: %s, %s" % (cows[0:move[0]-1], cows[(move[1]-1):(move[0]-2):-1], cows[move[1]:], move[1]-1, move[0]-2))
        
        
        temp = cows[0:move[0]-1]
        if move[0]-2 < 0:
            temp += cows[move[1]-1::-1]
        else:
            temp += cows[move[1]-1:move[0]-2:-1]
        
        temp += cows[move[1]:]
        
        cows = temp
        # print("after k: %d, move: %s ==> %s\n" % (k, move, cows))
print(*cows)
with open("swap.out", "w") as f:
    for i in cows:
        f.write("%d\n" % i)

