N, animals, charac = 0, [], []
with open("guess.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        temp = f.readline().split(" ")
        animals.append(temp[0])
        charac.append(list(i.strip("\n") for i in temp[2:]))

for i in range(N):
    print(animals[i], charac[i])

# key: feature
# val: list of animals
mapping = {} # Dictionary
for i in range(N):
    for f in charac[i]:
        if f not in mapping:
            mapping[f] = {animals[i]}
        else:
            mapping[f].add(animals[i])

for i in mapping:
    mapping[i] = len(mapping[i])

print("================\ncategories\n================")
for k, v in mapping.items():
    print(k, "\t", v)
print("================================\n\n")
# print("qr:", qr)

for i in range(N):
    changed = False
    for j in range(len(charac[i])-1, -1, -1):
        if mapping[charac[i][j]] == 1 and not changed:
            del charac[i][j]
            changed = True

lg = 0
for i in charac:
    if len(i) > lg:
        lg = len(i)

with open("guess.out", "w") as f:
    f.write("%s\n" % lg)