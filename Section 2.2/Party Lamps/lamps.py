"""
ID: pranav.19
LANG: PYTHON3
TASK: lamps
"""
import sys
# 0 --> off
# 1 --> on
# 2 --> arb
N = 0
finalC = 0
c = 0
bulbs = []
finalState = []
with open("lamps2.in", "r") as f:
    N = int(f.readline())
    finalC = int(f.readline())
    on = f.readline().split()
    off = f.readline().split()
    bulbs = [1 for i in range(N)]
    finalState = [2 for i in range(N)]
    for i in on[:len(on)-1]:
        finalState[int(i)-1] = 1
    for i in off[:len(off)-1]:
        finalState[int(i)-1] = 0

# print(*bulbs)
# print("finalState", *finalState)

goods = set([])
used = set([])
sys.setrecursionlimit(40000)
# Alternate span

def span(bulbState, c):
    global goods, finalC
    # if bulbState == [0 for i in range(N)]:
    #     print("Found one, c=%s" % c)
    if c == finalC:
        for i in finalState:
            if i != 2:
                break
        else:
            goods.add(tuple(bulbState))
            return
        for i in range(len(finalState)):
            if finalState[i] != 2 and not finalState[i] == bulbState[i]:
                break
        else:
            goods.add(tuple(bulbState))
        return
    elif tuple([tuple(bulbState), c]) in used:
        return
    
    used.add(tuple([tuple(bulbState), c]))

    # Button 1
    b1 = [(i+1)%2 for i in bulbState]
    # if b1 == [0 for i in range(N)]:
    #     print("%s made full 0, c = %s" % (bulbState, c))
    span(b1, c+1)

    # Button 2
    b2 = bulbState.copy()
    for i in range(0, len(b2), 2):
        b2[i] = (b2[i]+1)%2
    # if b2 == [0 for i in range(N)]:
    #     print("%s made full 0, c = %s" % (bulbState, c))
    span(b2, c+1)

    # Button 3
    b3 = bulbState.copy()
    for i in range(1, len(b3), 2):
        b3[i] = (b3[i]+1)%2
    # if b3 == [0 for i in range(N)]:
    #     print("%s made full 0, c = %s" % (bulbState, c))
    span(b3, c+1)

    # Button 4
    b4 = bulbState.copy()
    for i in range(0, len(b4), 3):
        b4[i] = (b4[i]+1)%2
    # if b4 == [0 for i in range(N)]:
    #     print("%s made full 0, c = %s" % (bulbState, c))
    span(b4, c+1)

span(bulbs, 0)
answers = []
for i in goods:
    answers.append("".join([str(j) for j in i]))

answers.sort()
for i in answers:
    print(i)

with open("lamps.out", "w") as f:
    if len(answers) == 0:
        f.write("IMPOSSIBLE\n")
    else:
        for i in answers:
            f.write("%s\n" % i)