"""
ID: pranav.19
LANG: PYTHON3
TASK: crypt1
"""
N, digits = 0, []
with open("crypt1.in", "r") as f:
    N = int(f.readline())
    temp = f.readline().split(" ")
    for d in range(N):
        digits.append(int(temp[d]))

S = 0
# print(N, digits)

def check(n1, n2):
    product = str(n1*n2)
    partial1 = str(n1*int(str(n2)[1]))
    partial2 = str(n1*int(str(n2)[0]))
    if len(product) == 4 and len(partial1) == 3 and len(partial2) == 3:
        # print(n1, n2, partial1, partial2, product)
        for i in product:
            if int(i) not in digits:
                return False
        for i in partial1:
            if int(i) not in digits:
                return False
        for i in partial2:
            if int(i) not in digits:
                return False
        return True
    else:
        return False
st = []
def debugCheck(n1, n2):
    product = str(n1*n2)
    partial1 = str(n1*int(str(n2)[1]))
    partial2 = str(n1*int(str(n2)[0]))
    # print("checking -->", n1, n2, partial1, partial2, product)
    if len(product) == 4 and len(partial1) == 3 and len(partial2) == 3:
        for i in product:
            if int(i) not in digits:
                print(i)
                return False
        for i in partial1:
            if int(i) not in digits:
                return False
        for i in partial2:
            if int(i) not in digits:
                return False
        statement = "works --> %s %s %s %s %s" % (
            n1, n2, partial1, partial2, product)
        print(statement)
        st.append(statement)
        return True        
    else:
        return False

nTop, nBottom = [], []

if N >= 1:
    for a in digits:
        for b in digits:
            for c in digits:
                nTop.append(int("{0:d}{1:d}{2:d}".format(a, b, c)))
            
    for a in digits:
        for b in digits:
            nBottom.append(int("{}{}".format(a, b)))

    solutions = []
    # print(nTop)
    # print(nBottom)

    for a in nTop:
        for b in nBottom:
            # print(check(a, b))
            # print(debugCheck(a, b))
            if check(a, b):
                S += 1
                solutions.append([a, b])
                

# print(nTop)
# print(nTop[0], nBottom[0], check(nTop[0], nBottom[0]))
# print("final check:", check(222, 22))

# print(S)
# print(solutions)
# print(S)
# for i in st:
#     print(i)
with open("crypt1.out", "w") as f:
    f.write("%s\n" % S)
