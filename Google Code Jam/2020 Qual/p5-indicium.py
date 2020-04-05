T = int(input())

def test(N, K):
    permutations = getPermutations("", {str(i) for i in range(1, N+1)}, set())
    # print("PERMUTATIONS (%s): %s" % (len(permutations), permutations))
    matrix = generateMatrix(N, K, permutations, [], set())
    return matrix

    # for matrix in allMatrices:
    #     print("Another (trace: %s):" % getTrace(N, matrix))
    #     print(matrix)

def getTrace(N, matrix):
    s = 0
    for i in range(0, len(matrix)):
        s += int(matrix[i][i])

    return s

    # if N % 2 == 0:
    #     return sum(nums)*2
    # else:
    #     return sum(nums[:len(nums)-1])*2+nums[len(nums)-1]

def generateMatrix(N, K, permutations, currentMatrix, allMatrices):
    # currentMatrix is an array of strings
    if len(currentMatrix) == N:
        # print("created matrix")
        if getTrace(N, currentMatrix) == K:
            return currentMatrix
        else:
            return None
        # allMatrices.add("".join(currentMatrix))
    
    else:
        for i in permutations:
            if len(currentMatrix) == 0:
                currentMatrix.append(i)
                e = generateMatrix(N, K, permutations, currentMatrix, allMatrices)
                if e != None:
                    return e
                del currentMatrix[len(currentMatrix)-1]
            else:
                for j in range(N):
                    if currentMatrix[len(currentMatrix)-1][j] == i[j]:
                        break
                else:
                    currentMatrix.append(i)
                    e = generateMatrix(N, K, permutations, currentMatrix, allMatrices)
                    if e != None:
                        return e
                    del currentMatrix[len(currentMatrix)-1]
            

    return None
    
def getPermutations(n, remainingSet, total):
    if len(remainingSet) == 0:
        total.add(n)
    else:
        for i in remainingSet:
            getPermutations(n+i, remainingSet - {i}, total)

    return total

for t in range(T):
    N, K = [int(i) for i in input().split(" ")]
    ans = test(N, K)
    if ans != None:
        print("Case #%s: POSSIBLE" % (t+1))
        for m in ans:
            print(" ".join([str(i) for i in m]))
    else:
        print("Case #%s: IMPOSSIBLE" % (t+1))