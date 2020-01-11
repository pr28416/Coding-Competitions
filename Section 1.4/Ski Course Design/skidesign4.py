"""
ID: pranav.19
LANG: PYTHON3
TASK: skidesign
"""

N = 0
oldHills = []

def average(n):
    return sum(n)/len(n)

def getPrice(n):
    t = 0
    for i in range(N):
        t += (n[i]-oldHills[i])**2
    return t

with open("skidesign.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        oldHills.append(int(f.readline()))

newHills = oldHills.copy()

# # Do step 1
# change = (newHills[myMax]-newHills[myMin]-17)
# xChange = int(change/2)
# yChange = change-xChange
# newHills[myMin] = newHills[myMin]+xChange
# newHills[myMax] = newHills[myMax]-yChange

def solve(o, n, low, up):
    old = [i for i in o]
    new = [i for i in n]
    # Get smallest, largest
    myMin = new.index(min(new))
    myMax = new.index(max(new))
    # Do step new 1
    avg = int(average(old))
    # print("avg =", avg)
    # Do step 1.1
    new[myMin] = avg - low
    new[myMax] = avg + up

    # Do step 2-4
    for i in range(N):
        if i != myMax and i != myMin:
            if old[i] <= new[myMin]: new[i] = new[myMin]
            elif old[i] >= new[myMax]: new[i] = new[myMax]

    # print(new)
    return getPrice(new)

prices = []

for i in range(1, 17):
    answer = solve(oldHills, newHills, i, 17-i)
    # print("lower: %s, upper: %s, answer: %s" % (i, 17-i, answer))
    # print(newHills)
    prices.append(answer)

# print(oldHills)
# print("Max[%s]: %s, Min[%s]: %s" % (myMin, newHills[myMin], myMax, newHills[myMax]))
# print(newHills)


# print("\n\n",prices)
with open("skidesign.out", "w") as f:
    # print(min(prices))
    f.write("{}\n".format(min(prices)))