"""
ID: pranav.19
LANG: PYTHON3
TASK: transform
"""
N = 0
prevSquare = []
newSquare = []
with open("transform.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        prevLine = str(f.readline())[:N]
        prevSquare.append([i for i in prevLine])
    for i in range(N):
        newLine = str(f.readline())[:N]
        newSquare.append([i for i in newLine])
        
def deg90(square):
    # print("1: deg90 ----------------------")
    # print("prev:")
    # printSquare(square)
    new = []
    i = 0
    while i < N:
        temp = []
        for j in range(N-1, -1, -1):
            temp.append(square[j][i])
        new.append(temp)
        i += 1
    # print("new:")
    # printSquare(new)
    return new

def deg180(square):
    # print("2: deg180 ----------------------")
    # print("prev:")
    # printSquare(square)
    temp = square.copy()
    temp = deg90(temp)
    temp = deg90(temp)
    # print("new:")
    # printSquare(temp)
    return temp

def deg270(square):
    # print("3: deg270 ----------------------")
    # print("prev:")
    # printSquare(square)
    temp = square.copy()
    temp = deg90(temp)
    temp = deg90(temp)
    temp = deg90(temp)
    # print("new:")
    # printSquare(temp)
    return temp

def reflect(square):
    # print("4: Reflect ----------------------")
    # print("orig:")
    # printSquare(square)
    new = []
    new = square.copy()
    for i in range(N):
        new[i] = new[i][::-1]

    # print("new:")
    # printSquare(new)
    # print("before:")
    # printSquare(square)
    return new

def combine(square, num):
    # print("5: Combine ----------------------")
    # print("orig:")
    # printSquare(square)
    t1 = square.copy()
    # print("t1:")
    # printSquare(t1)
    # printSquare(t1)
    t2 = reflect(t1)
    # print("t2:")
    # printSquare(t2)
    t3 = []
    # print("t3 before:")
    # printSquare(t3)
    if num == 1:
        t3 = deg90(t2)
    elif num == 2:
        t3 = deg180(t2)
    else:
        t3 = deg270(t2)
    # print("t3 after:")
    # printSquare(t3)
    return t3

def noChange(square, new):
    return square == new

def printSquare(sq):
    square = sq
    for i in square:
        for j in i:
            print(j, end=" ")
        print("", end="\n")

# print("Starting old")
# printSquare(prevSquare)

# print("Finishing new")
# printSquare(newSquare)

# printSquare(prevSquare)
# t1 = prevSquare.copy()
# t1 = reflect(t1)
# printSquare(t1)
# printSquare(prevSquare)
# t2 = t1.copy()
# t2 = reflect(t2)
# printSquare(t2)
# printSquare(t1)
# printSquare(prevSquare)

stepList = []

temp = deg90(prevSquare)
if newSquare == temp:
    stepList.append(1)

temp.clear()
temp = deg180(prevSquare)
if newSquare == temp:
    stepList.append(2)

temp.clear()
temp = deg270(prevSquare)
if newSquare == temp:
    stepList.append(3)

temp.clear()
temp = reflect(prevSquare)
if newSquare == temp:
    stepList.append(4)

temp.clear()
temp = combine(prevSquare, 1)
if newSquare == temp:
    stepList.append(5)

temp.clear()
temp = combine(prevSquare, 2)
if newSquare == temp:
    stepList.append(5)

temp.clear()
temp = combine(prevSquare, 3)
if newSquare == temp:
    stepList.append(5)

temp.clear()
if noChange(prevSquare, newSquare):
    stepList.append(6)

stepList.append(7)
# print(stepList)
# print(min(stepList))
with open("transform.out", "w") as f:
    f.write("%s\n" % min(stepList))
