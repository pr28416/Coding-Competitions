N, animals, charac = 0, [], []
with open("guess.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        temp = f.readline().split(" ")
        animals.append(temp[0])
        charac.append(set(i.strip("\n") for i in temp[2:]))

# for i in range(N):
#     print(animals[i], charac[i])

# key: feature
# val: set of animals
mapping = {} # Dictionary
qr = ""
for i in range(N):
    for f in charac[i]:
        if f not in mapping:
            mapping[f] = {animals[i]}
        else:
            mapping[f].add(animals[i])
        qr = f

print("================\ncategories\n================")
for k, v in mapping.items():
    print(k, "\t", v)
print("================================\n\n")
# print("qr:", qr)


# Start with a set of possible animals
possible = set(animals) # Set
count = 0
while len(possible) > 1:
    count += 1
    qr = list(mapping.keys())[0]
    for f in mapping:
        if len(possible.intersection(mapping[f])) > len(possible.intersection(mapping[qr])):
            qr = f
    # print("PUTS:\t", qr, "\tANIMALS:\t", mapping[qr])
    print("PUTS:\t", qr)
    # break
    possible &= mapping[qr]
    del mapping[qr]
    # print(possible)

print("YOU PICKED ANIMAL:", possible.pop())
print("YES COUNT:", count)

with open("guess.out", "w") as f:
    f.write("%s\n" % count)