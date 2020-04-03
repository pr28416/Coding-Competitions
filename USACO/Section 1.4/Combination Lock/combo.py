"""
ID: pranav.19
LANG: PYTHON3
TASK: combo
"""
N = 0
johnCombo = []
masterCombo = []
with open("combo.in", "r") as f:
    N = int(f.readline())
    johnCombo = f.readline().split(" ")
    for i in range(3):
        johnCombo[i] = int(johnCombo[i])
    masterCombo = f.readline().split(" ")
    for i in range(3):
        masterCombo[i] = int(masterCombo[i])

# print(N, johnCombo, masterCombo)
workingCombinations = []

for i in range(0, len(johnCombo)):
    for a in range(-2, 3):
        for j in range(0, i):
            for b in range(-2, 3):
                for k in range(0, j):
                    for c in range(-2, 3):
                        testCombo = [(johnCombo[i]+a) % N, (johnCombo[j]+b) % N, (johnCombo[k]+c) % N]
                        if testCombo not in workingCombinations:
                            workingCombinations.append(testCombo)
                        testCombo = [(masterCombo[i]+a) % N, (masterCombo[j]+b) % N, (masterCombo[k]+c) % N]
                        if testCombo not in workingCombinations:
                            workingCombinations.append(testCombo)

with open("combo.out", "w") as f:
    f.write("{}\n".format(len(workingCombinations)))