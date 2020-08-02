"""
ID: pranav.19
LANG: PYTHON3
TASK: money
"""
# DP solution

V = N = coinTypes = None
with open("money.in", "r") as f:
    V, N = map(int, f.readline().split(" "))
    coinTypes = {0}
    temp = f.readline()
    while temp != None and len(temp) != 0:
        coinTypes |= set(map(int, temp.split(" ")))
        temp = f.readline()
    coinTypes = sorted(list(coinTypes))

dp = [[0 for i in range(N+1)] for j in range(len(coinTypes))]
dp[0][0] = 1

for row in range(1, len(coinTypes)):
    back = 0
    for col in range(N+1):
        if col < coinTypes[row]:
            dp[row][col] = dp[row-1][col]
            continue
        else:
            dp[row][col] = dp[row-1][col] + dp[row][back]
            back += 1

with open("money.out", "w") as f:
    f.write("%s\n" % dp[len(dp)-1][len(dp[0])-1])