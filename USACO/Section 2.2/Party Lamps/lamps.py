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
bulbs = ""
finalState = []
with open("lamps3.in", "r") as f:
    N = int(f.readline())
    finalC = int(f.readline())
    on = f.readline().split()
    off = f.readline().split()
    for i in range(N):
        bulbs += "1"
        finalState.append("2")

    for i in on[:len(on)-1]:
        finalState[int(i)-1] = "1"
    for i in off[:len(off)-1]:
        finalState[int(i)-1] = "0"
    finalState = "".join(finalState)
# print(*bulbs)
# print("finalState", *finalState)

goods = set([])
used = set([])
sys.setrecursionlimit(40000)
# Alternate span

def span(bulbState, c, lastUsed):
    global goods, finalC
    for i in range(c, finalC, 4):
        if str(i)+"-"+bulbState in used:
            print("poopy")
            return

    if c == finalC:
        for i in finalState:
            if i != "2":
                break
        else:
            goods.add(bulbState)
            return
        
        for i in range(len(finalState)):
            # print(len(finalState) == len(bulbState))
            if finalState[i] != "2" and not finalState[i] == bulbState[i]:
                return

        goods.add(bulbState)
        return
    elif str(c)+"-"+bulbState in used:
        return
    
    used.add(str(c)+"-"+bulbState)

    b1 = "".join([str((int(i)+1)%2) for i in bulbState])
    b2 = ""
    for i in range(0, len(bulbState)):
        if i % 2 == 1:
            b2 += str((int(bulbState[i])+1)%2)
        else:
            b2 += bulbState[i]
    b3 = ""
    for i in range(0, len(bulbState)):
        if i % 2 == 0:
            b3 += str((int(bulbState[i])+1)%2)
        else:
            b3 += bulbState[i]
    b4 = ""
    for i in range(0, len(bulbState)):
        if i % 3 == 0:
            b4 += str((int(bulbState[i])+1)%2)
        else:
            b4 += bulbState[i]
    # print(len(b1) == len(bulbState))
    # print(len(b2) == len(bulbState))
    # print(len(b3) == len(bulbState))
    # print(len(b4) == len(bulbState))
    # print("\t"*c+"b_: "+bulbState)
    # print("\t"*c+"b1: "+b1)
    # print("\t"*c+"b2: "+b2)
    # print("\t"*c+"b3: "+b3)
    # print("\t"*c+"b4: "+b4)
    if lastUsed not in {1, 2, 3, 4}:
        print("something wrong meanie poopy: %s" % lastUsed)
    if lastUsed == 4:
        span(b4, c+1, 4)
    elif lastUsed == 3:
        span(b3, c+1, 3)
        span(b4, c+1, 3)
    elif lastUsed == 2:
        span(b2, c+1, 2)
        span(b3, c+1, 2)
        span(b4, c+1, 2)
    elif lastUsed == 1:
        span(b1, c+1, 1)
        span(b2, c+1, 1)
        span(b3, c+1, 1)
        span(b4, c+1, 1)

    return

span(bulbs, 0, 1)
answers = []
for i in goods:
    answers.append(i)

answers.sort()
for i in answers:
    print(i)

with open("lamps.out", "w") as f:
    if len(answers) == 0:
        f.write("IMPOSSIBLE\n")
    else:
        for i in answers:
            f.write("%s\n" % i)