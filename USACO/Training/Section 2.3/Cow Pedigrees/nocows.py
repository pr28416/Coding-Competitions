with open("nocows.in") as f:
    N, K = map(int, f.readline().split(" "))

N0, K0 = (N-1)//2, K-1

# Create dp array
dp = [[0] * K0 for _ in range(N0)]
dp[0][0] = 1

# Populate last cases
for i in range(1, min(N0, K0)):
    dp[i][i] = 2**(i-1)

# for i in dp:
#     print(*i)

for n in range(N0):
    for k in range(K0):
        # DP value already filled
        if dp[n][k] != 0: continue

        # Case 1: Left subtree height = k-1, right subtree height < k-1
        # Iterate through 
        # Case 2: Right subtree height = k-1, left subtree height < k-1
        # Case 3: Left subtree height = k-1, right subtree height = k-1