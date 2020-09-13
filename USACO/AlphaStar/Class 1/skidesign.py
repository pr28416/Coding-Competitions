N, hills = None, None
with open("skidesign.in") as f:
    N = int(f.readline())
    hills = [int(f.readline()) for _ in range(N)]

hills.sort()
new = hills.copy()
print(N, hills)

lo, up = 0, len(new)-1

while abs(new[up] - new[lo]) > 17:
    if lo == len(new)-1: break
    if up == 0: break

    if lo > len(new)-up:
        # Increase lower bounds
        if new[lo] == new[lo+1]:
            lo += 1
            continue
        else:
            new[lo] += 1
    else:
        # Decrease upper bounds
        if new[up] == new[up-1]:
            up -= 1
            continue
        else:
            new[up] -= 1

for i in range(lo):
    new[i] = new[lo]

for i in range(up+1, len(new)):
    new[i] = new[up]

print(new)
