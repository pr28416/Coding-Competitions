"""
ID: pranav.19
LANG: PYTHON3
TASK: preface
"""
N = 0
with open("preface.in", "r") as f:
    N = int(f.readline())

numToLetter = {
    1:      "I",
    5:      "V",
    10:     "X",
    50:     "L",
    100:    "C",
    500:    "D",
    1000:   "M"
}

def numeral(n):
    # print(n)
    basePairs, groupedPairs = [], [[]]
    a, b = n, [i for i in reversed(sorted(numToLetter.keys()))]
    while a > 0:
        if a >= b[0]:
            basePairs.append(b[0])
            a -= b[0]
        else:
            del b[0]
    for i in basePairs:
        if len(groupedPairs[0]) == 0:
            groupedPairs[0].append(i)
        elif len(str(groupedPairs[len(groupedPairs)-1][0])) == len(str(i)):
            groupedPairs[len(groupedPairs)-1].append(i)
        else:
            groupedPairs.append([i])
    # print(*groupedPairs)
    finalStr = ""
    for i in groupedPairs:
        l = 0
        if str(i[0])[0] == "5":
            l = 1
        if len(i)-l == 4:
            finalStr += str(numToLetter[i[1]])
            # print(finalStr)
            if l == 1:
                finalStr += str(numToLetter[i[0]*2])
                # print(finalStr)
            else:
                finalStr += str(numToLetter[i[0]*5])
        else:
            if l == 1:
                finalStr += str(numToLetter[i[0]]) + str(numToLetter[i[len(i)-1]])*(len(i)-l)
            else:
                finalStr += str(numToLetter[i[len(i)-1]])*(len(i)-l)
    # print(n, "\t-->", finalStr)
    return finalStr

f = {
    "I": 0,
    "V": 0,
    "X": 0,
    "L": 0,
    "C": 0,
    "D": 0,
    "M": 0
}
for i in range(1, N+1):
    a = numeral(i)
    for i in a:
        f[i] += 1

with open("preface.out", "w") as e:
    d = True
    for (key, val) in f.items():
        if int(val) != 0:
            d = False
            e.write("%s %s\n" % (key, val))
    if d:
        e.write("\n")