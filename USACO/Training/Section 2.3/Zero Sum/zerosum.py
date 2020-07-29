"""
ID: pranav.19
LANG: PYTHON3
TASK: zerosum
"""
N, original = None, []
with open("zerosum.in", "r") as f:
    N = int(f.readline())
    for i in range(1, N+1):
        original.extend([str(i), ''])
    original.pop()

def solve(expr):
    array = []
    current = ""
    nextOperation = None
    for i in expr:
        if i == "+" or i == "-":
            array.append(int(current))
            array.append(i)
            current = ""
        elif i == " ":
            continue
        else:
            current += i
    array.append(int(current))

    while len(array) > 2:
        if array[1] == "+":
            array[2] += array[0]
        else:
            array[2] = array[0] - array[2]
        array.pop(0)
        array.pop(0)
    
    return int("".join(map(str, array)))

expressions = []

def recurse(expr, i):
    global expressions
    if i >= len(expr):
        e = "".join(expr)
        if solve(e) == 0:
            expressions.append(e)
    else:
        for c in ["+", "-", ' ']:
            expr[i] = c
            recurse(expr, i+2)
            expr[i] = ''

recurse(original, 1)
expressions.sort()
with open("zerosum.out", "w") as f:
    for i in expressions:
        f.write("%s\n" % i)