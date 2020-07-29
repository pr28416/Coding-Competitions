N, bessie, elsie, relationships = [None] * 4
txt = "family.in"
# txt = "family_bronze_open18/7.in"

with open(txt, "r") as f:
    N, bessie, elsie = [i.strip("\n") for i in f.readline().split(" ")]
    N, relationships = int(N), []
    for i in range(N):
        relationships.append([i.strip("\n") for i in f.readline().split(" ")])

# print(N, bessie, elsie)

motherOf = {i[1]:i[0] for i in relationships}
for i in motherOf:
    print(i, motherOf[i])

def writeln(message):
    with open("family.out", "w") as f:
        f.write("%s\n" % message)

import sys

# Cases:
# BESSIE and ELSIE are SIBLINGS
if bessie in motherOf and elsie in motherOf and motherOf[bessie] == motherOf[elsie]:
    writeln("SIBLINGS")
    sys.exit()

# BESSIE is a direct descendant of ELSIE
def checkDescendant(bessie, elsie):
    child = bessie
    status = 1 # 1 = mother, 2 = grand-mother, 3 = great-grandmother, ...
    found = False
    while child in motherOf:
        if motherOf[child] == elsie:
            found = True
            break
        child = motherOf[child]
        status += 1

    if found:
        if status == 1: writeln("%s is the mother of %s" % (elsie, bessie))
        elif status == 2: writeln("%s is the grand-mother of %s" % (elsie, bessie))
        else:
            older = ""
            for i in range(status - 2):
                older += "great-"
            writeln("%s is the %sgrand-mother of %s" % (elsie, older, bessie))
        sys.exit()

checkDescendant(bessie, elsie)
checkDescendant(elsie, bessie)

def checkAunt(bessie, elsie):
    child = None
    # ELSIE is an aunt (or older) of BESSIE
    try: child = motherOf[bessie]
    except: child = None
    if elsie not in motherOf: return

    status, found = 0, False # 0 = aunt, 1 = great-aunt, 2 = great-great-aunt, ...
    print("starting child at", child)
    while child in motherOf:
        print("is the mother of %s (%s) the mother of %s (%s)?" % (
            child, motherOf[child], elsie, motherOf[elsie]
        ), end=" ")
        if motherOf[child] == motherOf[elsie]:
            print("Yes")
            found = True
            break
        print("No")
        child = motherOf[child]
        status += 1

    if found:
        writeln("%s is the %saunt of %s" % (elsie, status * "great-", bessie))
        sys.exit()

checkAunt(bessie, elsie)
checkAunt(elsie, bessie)

# ELSIE and BESSIE are COUSINS
found = False
bessieAncestor = bessie
while bessieAncestor in motherOf:
    elsieAncestor = elsie
    while elsieAncestor in motherOf:
        if motherOf[bessieAncestor] == motherOf[elsieAncestor]:
            found = True
            break
        elsieAncestor = motherOf[elsieAncestor]
    else:
        bessieAncestor = motherOf[bessieAncestor]
        continue
    break

if found:
    writeln("COUSINS")
    sys.exit()

# ELSIE and BESSIE are not related
writeln("NOT RELATED")
sys.exit()