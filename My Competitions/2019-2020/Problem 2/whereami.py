# N --> number of houses
N = 0
mailboxes = ""

with open("whereami.in", "r") as f:
    N = int(f.readline())
    mailboxes = f.readline()

# print(N, mailboxes)

# i = 0, k = 3
finalK = N
# print(finalK)
# Iterate through k
didFind = False
for k in range(N, 0, -1):
    # Iterate through possible combinations of length k
    didWork = True
    for i in range(N-k):

        # End index is i+k
        seq = mailboxes[i:i+k]

        # Check all other substrings after this particular one to see if they are identical
        for x in range(i+1, N-k+1):
            item = mailboxes[x:x+k]
            if seq == item:
                didWork = False
                break
        else:
            continue
    if didWork and k < finalK:
        finalK = k

with open("whereami.out", "w") as f:
    f.write("%s\n" % finalK)