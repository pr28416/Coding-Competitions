cows = [int(input()) for _ in range(12)]

minSkill = None
def recurse(a, w, b, x, c, y, d, z, i):
    global cows, minSkill
    if i == len(cows):
        e = max(a, b, c, d)-min(a, b, c, d)
        if minSkill is None or e < minSkill:
            minSkill = e
    else:
        if w < 3: recurse(a+cows[i], w+1, b, x, c, y, d, z, i+1)
        if x < 3: recurse(a, w, b+cows[i], x+1, c, y, d, z, i+1)
        if y < 3: recurse(a, w, b, x, c+cows[i], y+1, d, z, i+1)
        if z < 3: recurse(a, w, b, x, c, y, d+cows[i], z+1, i+1)

recurse(*((0,)*9))
print(minSkill)