"""
ID: pranav.19
LANG: PYTHON3
TASK: money
"""

V = N = coinTypes = None
with open("money.in", "r") as f:
    V, N = map(int, f.readline().split(" "))
    coinTypes = sorted(list(map(int, f.readline().split(" "))), reverse=True)

# print(V, N)

print("coin types:", *coinTypes, f"need to construct {N}")
steps = 0
def count(amount, total, coinTypes, coinIdx):
    global steps
    if amount == total:
        # print("Found amount early")
        steps += 1
        return 1
    if coinIdx >= len(coinTypes):
        steps += 1
        if amount == total:
            # print("\t"*coinIdx, "worked")
            return 1
        return 0

    else:
        maxCoins = int((total-amount)/coinTypes[coinIdx])
        if maxCoins <= 0:
            return count(amount, total, coinTypes, coinIdx+1)
        s = 0
        minCoins = 0
        if coinIdx == len(coinTypes)-1:
            minCoins = int((total-amount))
        for i in range(maxCoins+1):
            steps += 1
            # print("\t" * coinIdx,"adding %s coins of %s" % (i, coinTypes[coinIdx]))
            s += count(amount + coinTypes[coinIdx] * i, total, coinTypes, coinIdx+1)
        return s

x = count(0, N, coinTypes, 0)
print(f"Answer: {x}, steps: {steps}")
with open("money.out", "w") as f:
    f.write("%s\n" % x)