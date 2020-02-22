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
with open("lamps.in", "r") as f:
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

def button1(s):
    return "".join([str((int(i)+1)%2) for i in s])

def button2(s):
    b2 = ""
    for i in range(0, len(s)):
        if i % 2 == 1:
            b2 += str((int(s[i])+1)%2)
        else:
            b2 += s[i]
    return b2

def button3(s):
    b3 = ""
    for i in range(0, len(s)):
        if i % 2 == 0:
            b3 += str((int(s[i])+1)%2)
        else:
            b3 += s[i]
    return b3

def button4(s):
    b4 = ""
    for i in range(0, len(s)):
        if i % 3 == 0:
            b4 += str((int(s[i])+1)%2)
        else:
            b4 += s[i]
    return b4

previousList = {}
currentList = {bulbs}

for c in range(finalC):
    previousList = currentList.copy()
    temp = set([])

    for i in currentList:
        temp.add(button1(i))
        temp.add(button2(i))
        temp.add(button3(i))
        temp.add(button4(i))

    if len(previousList - temp) == 0 and len(temp - previousList) == 0:
        break

    currentList = temp

for state in currentList:
    for i in finalState:
            if i != "2":
                break
    else:
        goods.add(state)
    
    for i in range(len(finalState)):
        # print(len(finalState) == len(bulbState))
        if finalState[i] != "2" and not finalState[i] == state[i]:
            break
    else:
        goods.add(state)
# print("Ended checks")

answers = []
for i in goods:
    answers.append(i)

answers.sort()
# for i in answers:
#     print(i)
with open("lamps.out", "w") as f:
    if len(answers) == 0:
        f.write("IMPOSSIBLE\n")
    else:
        for i in answers:
            f.write("%s\n" % i)