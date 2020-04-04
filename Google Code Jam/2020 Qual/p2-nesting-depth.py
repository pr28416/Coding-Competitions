# T: # Test cases
T = int(input())

# Splits first string into individual groups
def splitIntoParts(S):
    # Arrange into groups
    arr = [S[0]]
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            arr[len(arr)-1] += S[i]
        else:
            arr.append(S[i])

    return arr

# Gets all nonzero subarrays in an array
def getSubarrays(arr):
    # Make sure arr length is not
    assert len(arr) != 0

    # Break into subarrays
    r = [[arr[0]]]
    if arr[0] == 0:
        r.append([])
    for i in range(1, len(arr)):
        if arr[i] == 0:
            r.append([0])
            if i != len(arr)-1:
                r.append([])
        else:
            r[len(r)-1].append(arr[i])
    
    if len(r[len(r)-1]) == 0:
        del r[len(r)-1]

    return r

# Subtracts n from every single element in array
def subtractFromAll(arr, n):
    for i in range(len(arr)):
        arr[i] -= n

# Checks if all elements are 0
def containsOnlyZeros(arr):
    for i in arr:
        if i != 0:
            return False
    return True


# def test(S)
    
# Main recursion function
def recursionFunc(arr, depth):
    # print("\n"+" "*depth+"starting with %s" % arr)
    
    if containsOnlyZeros(arr):
        # print(" "*depth+"contained only zeros")
        # for i in range(len(arr)):
        #     arr[i] += 1
        return arr

    # 1: Subtract 1 from all
    subtractFromAll(arr, 1)
    # print(" "*depth+"subtracting to %s" % arr)
    # 2: Get subarrays
    subarr = getSubarrays(arr)
    # print(" "*depth+"extracting subarrays: %s" % subarr)
    # 3: For each subarray, recurse through and replace spot
    for i in range(len(subarr)):
        # print(" "*depth+"subarr %s: %s" % (i, subarr[i]))
        e = subarr[i]
        subarr[i] = recursionFunc(subarr[i], depth+1)
        # print("  "*depth+"returned subarr %s from orig: %s" % (subarr[i], e))
        # for j in range(len(subarr[i])):
        #     print("  "*depth+"i", subarr[i])
        #     print("  "*depth+"j", subarr[i][j])
        #     subarr[i][j] += 1
        # print("  "*depth+"added 1 to subarr: %s" % subarr[i])

    for i in range(len(subarr)-1, -1, -1):
        if len(subarr[i]) == 0:
            del subarr[i]
    
    return subarr


def traversionFunc(arr, depth):
    global newStr
    if arr == [0]:
        newStr += str(depth)
    else:
        newStr += "("
        for i in arr:
            traversionFunc(i, depth+1)
        
        newStr += ")"




finalStr = ""
newStr = ""

for t in range(T):
    # Get input

    # Do something with input
    data = [int(i) for i in input()]

    e = getSubarrays(data)
    # print("MAIN SUBARRAYS: %s" % e)
    finalStr = ""
    newStr = ""
    for sub in e:
        if containsOnlyZeros(sub):
            finalStr += "0"*len(sub)
        else:
            newStr = ""
            f = recursionFunc(sub, 0)
            traversionFunc(f, 0)
            finalStr += newStr
    
    # Print output
    print("Case #%s: %s" % (t+1, finalStr))