# General algorithm for window sliding
# Find max sum in this case of K consecutive
N, K = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))

lo, up = 0, K-1
maxSum = 0

# Get initial sum
for i in range(K):
    maxSum += numbers[i]

# Window sliding
curSum = maxSum
while up < N:
    # Subtract the old lower bound
    curSum -= numbers[lo]
    # Shift the window
    lo += 1; up += 1
    # Make sure range is still valid
    if up >= N: break
    # Add the new upper bound
    curSum += numbers[up]
    # Check if there is new max sum
    if curSum > maxSum: maxSum = curSum

print(maxSum)