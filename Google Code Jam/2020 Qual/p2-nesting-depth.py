# T: # Test cases
T = int(input())


def test(S):
    # Arrange into groups
    arr = [S[0]]
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            arr[len(arr)-1] += S[i]
        else:
            arr.append(S[i])
    print(arr)

    usedIdx = set()
    curSmallest = 0

    # modifiedArr will contain the parentheses
    modifiedArr = [i for i in arr]
    numTimes = 0
    while numTimes < len(arr):
        # print("Still running: ")
        # Get smallest
        smallIdx = 0
        for i in range(len(arr)):
            if int(arr[i][0]) <= int(arr[smallIdx][0]) and i not in usedIdx:
                smallIdx = i
        
        usedIdx.add(smallIdx)
        
        # Span from smallest to see where parentheses can go
        # leftParIdx is on left of index, rightParIdx is on right of index
        leftParIdx, rightParIdx = smallIdx, smallIdx
        lowerBound, upperBound = 
        # Span leftParIdx
        while leftParIdx >= 0:
            if int(arr[leftParIdx][0]) >= int(arr[smallIdx][0]):
                if leftParIdx == 0:
                    break
                leftParIdx -= 1
            else:
                break
        
        # Span rightParIdx
        while rightParIdx <= len(arr):
            if int(arr[rightParIdx][0]) >= int(arr[smallIdx][0]):
                if rightParIdx == len(arr)-1:
                    break
                rightParIdx += 1
            else:
                break

        # Insert parentheses
        print("smallestIdx: %s, smallest: %s, leftParIdx: %s, rightParIdx: %s" % (smallIdx, arr[smallIdx], leftParIdx, rightParIdx+1))
        modifiedArr.insert(rightParIdx+1, ")")
        modifiedArr.insert(leftParIdx, "(")
        print(modifiedArr)
        print("".join(modifiedArr))
        print()
        numTimes += 1
        
    
    return "".join(modifiedArr)



for t in range(T):
    # Get input
    S = input()

    # Do something with input
    res = test(S)

    # Print output
    print(res)