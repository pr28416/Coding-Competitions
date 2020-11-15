V = int(input())
requirements = list(map(int, input().split(" ")))
G = int(input())
feedTypes = [list(map(int, input().split(" "))) for _ in range(G)]

totalOnes = V
bestAnswer = []
def subset(s, i, o):
    global bestAnswer, totalOnes, requirements, feedTypes, V, G
    if o > totalOnes: return
    elif i >= G:
        m = [0] * V
        for j in range(G):
            if s[j] == 0: continue
            for k in range(V): m[k] += feedTypes[j][k]
        for j in range(V):
            if requirements[j] > m[j]: return
        bestAnswer = [i+1 for i in range(G) if s[i]]
        totalOnes = o
    else:
        s[i] = 0; subset(s, i+1, o)
        s[i] = 1; subset(s, i+1, o+1)

subset([0]*G, 0, 0)
print(totalOnes, *sorted(bestAnswer))