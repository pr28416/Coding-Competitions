"""
ID: pranav.19
LANG: PYTHON3
TASK: milk3
"""

A_cap, B_cap, C_cap = 0, 0, 0

with open("milk3.in", "r") as f:
    temp = f.readline().split(" ")
    A_cap, B_cap, C_cap = int(temp[0]), int(temp[1]), int(temp[2])

caps = [A_cap, B_cap, C_cap]
buckets = [0, 0, C_cap]
visitedCombos = []
answers = []


def recurseThrough(currentCombo):
    for i in range(3):
        for k in range(3):
            if k != i:
                # Pour i into k
                change = 0
                if currentCombo[i] + currentCombo[k] > caps[k]:
                    change = caps[k] - currentCombo[k]
                    currentCombo[k] = caps[k]
                    currentCombo[i] -= change
                else:
                    change = currentCombo[i]
                    currentCombo[k] += currentCombo[i]
                    currentCombo[i] = 0

                # Check if exists; if so, stop. If not, recurse through new one
                if currentCombo not in visitedCombos:
                    visitedCombos.append(currentCombo.copy())
                    # Check if A = 0
                    if currentCombo[0] == 0:
                        answers.append(currentCombo[2])
                    recurseThrough(currentCombo)

                # Pour k back into i
                currentCombo[i] += change
                currentCombo[k] -= change


recurseThrough(buckets)

# print(answers)

answers.sort()

with open("milk3.out", "w") as f:
    phrase = ""
    for i in answers:
        phrase += ("%s " % i)
    phrase = phrase[0:len(phrase)-1]
    phrase += "\n"
    f.write(phrase)
