"""
ID: pranav.19
LANG: PYTHON3
TASK: dualpal
"""
N = 0
S = 0
with open("dualpal.in", "r") as f:
    txt = f.readline().split(" ")
    N, S = int(txt[0]), int(txt[1])

def convert(b, n):
    # print("starting new")
    new = ""
    number = n
    exp = 0
    while b**(exp+1) <= number:
        exp += 1
    while exp >= 0:
        remainder = number % (b**exp)
        # print(int(number//(b**exp)), b, number, b**exp, end="\t\t")
        new += "0123456789"[int(number//(b**exp))]
        number = remainder
        exp -= 1
    return new

def isDualPal(n):
    count = 0
    for b in range(2, 11):
        a = convert(b, n)
        if str(a) == str(a)[::-1]:
            count += 1
        if count == 2:
            return True
    else:
        return False

c = 0
output = ""
S += 1
while c < N:
    if isDualPal(S):
        output += "%s\n" % S
        c += 1
    S += 1

with open("dualpal.out", "w") as f:
    f.write(output)
