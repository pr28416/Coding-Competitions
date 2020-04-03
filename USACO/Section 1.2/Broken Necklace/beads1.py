"""
ID: pranav.19
LANG: PYTHON3
TASK: beads
"""
def beadNum(beadString):
    i = 0
    repeat = True
    while repeat and i < len(beadString)-1:
            if beadString[i] == beadString[i+1]:
                i += 1
            else:
                repeat = False
    return [beadString[0], i+1]

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str

def combine(arr1, arr2):
    if arr1[0] == arr2[0]:
        return [arr1[0], arr1[1]+arr2[1]]
    elif arr1[0] == "w":
        return [arr2[0], arr1[1]+arr2[1]]
    elif arr2[0] == "w":
        return [arr1[0], arr1[1]+arr2[1]]
    else:
        return None

beads = ""
N = 0
with open("beads.in", "r") as f:
    N = int(f.readline())
    beads = str(f.readline())

maxAmt = 0

for x in range(N):
    initString = beads[x:N] + beads[0:x]
    someString = initString
    out1 = []
    prevOut = []
    i = 0
    beadType = ""
    while i < len(initString):
        prevOut = out1
        out1 = beadNum(someString)
        if len(prevOut) > 0:
            if combine(prevOut, out1) is not None:
                if len(beadType) == 0:
                    i += out1[1]
                    out1 = combine(prevOut, out1)
                    beadType = out1[0]
                elif combine(prevOut, out1)[0] == beadType:
                    i += out1[1]
                    out1 = combine(prevOut, out1)
                else:
                    break
            else:
                break
        else:
            prevOut = out1
            i += out1[1]

        someString = initString[i:]
    
    r = prevOut[1]

    initString = someString[::-1]
    someString = initString
    out1 = []
    prevOut = []
    i = 0
    beadType = ""
    while i < len(initString):
        prevOut = out1
        out1 = beadNum(someString)
        if len(prevOut) > 0:
            if combine(prevOut, out1) is not None:
                if len(beadType) == 0:
                    i += out1[1]
                    out1 = combine(prevOut, out1)
                    beadType = out1[0]
                elif combine(prevOut, out1)[0] == beadType:
                    i += out1[1]
                    out1 = combine(prevOut, out1)
                else:
                    break
            else:
                break
        else:
            prevOut = out1
            i += out1[1]

        someString = initString[i:]
    
    if len(prevOut) == 0:
        l = 0
    else:
        l = prevOut[1]

    if maxAmt < l+r:
        maxAmt = l+r

with open("beads.out", "w") as f:
    f.write(str(maxAmt) + "\n")