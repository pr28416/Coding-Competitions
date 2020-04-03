"""
ID: pranav.19
LANG: PYTHON3
TASK: hamming
"""

N, B, D = 0, 0, 0
with open("hamming.in", "r") as f:
    temp = f.readline().split(" ")
    N, B, D = int(temp[0]), int(temp[1]), int(temp[2])

hammingNumbers = [0]

for i in range(1, 2**B):
    if len(hammingNumbers) >= N:
        break
    for j in hammingNumbers:
        if bin(i^j).count("1") < D:
            break
    else:
        hammingNumbers.append(i)

answers = []
while len(hammingNumbers) > 0:
    sub = []
    for i in range(10):
        if len(hammingNumbers) == 0:
            break
        sub.append(str(hammingNumbers.pop(0)))
    answers.append(sub)

with open("hamming.out", "w") as f:
    for i in answers:
        f.write(" ".join(i))
        f.write("\n")

