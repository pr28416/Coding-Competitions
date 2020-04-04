# T: # Test cases
T = int(input())

def test(N, matrix):

    # Calculate k
    k = 0

    for i in range(N):
        k += int(matrix[i][i])

    # Calculate r and c
    r, c = 0, 0
    for i in range(N):
        rset, cset = set(), set()
        rmod, cmod = False, False
        for j in range(N):
            if matrix[i][j] in rset and not rmod:
                r += 1
                rmod = True
            else:
                rset.add(matrix[i][j])
            
            if matrix[j][i] in cset and not cmod:
                c += 1
                cmod = True
            else:
                cset.add(matrix[j][i])

    return [k, r, c]

for t in range(T):
    # Get input
    N = int(input())
    matrix = []
    for n in range(N):
        matrix.append(input().split(" "))
    
    # Run test
    k, r, c = test(N, matrix)
    # k: trace of the matrix
    # r: num rows containing repeated elements
    # c: num cols containing repeated elements

    # Print result
    print("Case #%s: %s %s %s" % (t+1, k, r, c))