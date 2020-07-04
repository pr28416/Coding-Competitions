"""
ID: pranav.19
LANG: PYTHON3
TASK: namenum
"""
possibleNames = []
personSerial = 0

with open("namenum.in", "r") as f:
    personSerial = int(f.readline())

with open("dict.txt", "r") as f:
    possibleNames = [i for i in f.readlines() if len(i)-1 == len(str(personSerial))]

for i in range(len(possibleNames)):
    possibleNames[i] = possibleNames[i][:len(possibleNames[i])-1]

keypad = {
    "ABC": "2",
    "DEF": "3",
    "GHI": "4",
    "JKL": "5",
    "MNO": "6",
    "PRS": "7",
    "TUV": "8",
    "WXY": "9"
}

listOfNames = []

didFind = False
for name in possibleNames:
    translation = ""
    for letter in name:
        for key, value in keypad.items():
            if letter in key:
                translation += value
                break
    if translation == str(personSerial):
        didFind = True
        listOfNames.append(name)

finalNames = ""
for i in listOfNames:
    finalNames += "%s\n" % i

with open("namenum.out", "w") as f:
    if didFind:
        f.write(finalNames)
    else:
        f.write("NONE\n")