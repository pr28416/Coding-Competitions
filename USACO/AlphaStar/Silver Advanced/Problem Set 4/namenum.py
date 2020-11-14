N = int(input())
names = []
while True:
    try: e = input()
    except: break
    names.append(e)
names.sort()

def binSearch(x, lst):
    lo, up = 0, len(lst)
    while lo < up:
        y = (lo+up)//2
        if x == lst[y]: return True
        elif x < lst[y]: up=y
        else: lo=y+1
    return False

keypad = [list(i) for i in ["   ", "   ", "ABC", "DEF", "GHI", "JKL", "MNO", "PRS", "TUV", "WXY"]]
permutations = []

def permute(num, i, string):
    if i == len(num): permutations.append(string)
    else:
        for j in keypad[int(num[i])]:
            permute(num, i+1, string+j)

permute(str(N), 0, "")

didFind = False
for p in permutations:
    if binSearch(p, names): didFind = True; print(p)

if not didFind: print("NONE")