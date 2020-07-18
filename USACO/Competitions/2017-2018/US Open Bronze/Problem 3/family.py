N, bessie, elsie, relationships = [None] * 4
with open("family.in", "r") as f:
    N, bessie, elsie = [i.strip("\n") for i in f.readline().split(" ")]
    N, relationships = int(N), []
    for i in range(N):
        relationships.append([i.strip("\n") for i in f.readline().split(" ")])

print(N, bessie, elsie)

motherOf = {i[1]:i[0] for i in relationships}
for i in motherOf:
    print(i, motherOf[i])

def writeln(message):
    with open("family.out", "w") as f:
        f.write("%s\n" % message)

import sys

# Cases:
# BESSIE and ELSIE have the same mother
if motherOf[bessie] == motherOf[elsie]:
    writeln("SIBLINGS")
    sys.exit()

# BESSIE is a direct descendant of ELSIE
child = bessie
status = 1 # 1 = mother, 2 = grandmother, 3 = great-grandmother, ...
found = False
while child in motherOf:
    if motherOf[child] == elsie:
        found = True
        break
    child = motherOf[child]
    status += 1

if found:
    pass # TODO: Process status => relationship