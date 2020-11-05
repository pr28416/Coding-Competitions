# Calculates range sum
nums = list(map(int, input().split(" ")))
sums = [nums[0]]
print(nums)
q = int(input())
ranges = [tuple(map(int, input().split(" "))) for _ in range(q)]
for i in range(1, len(nums)):
    sums.append(sums[i-1]+nums[i])
print(sums)

for range in ranges:
    if range[0] > range[1]:
        print("Invalid input")
        continue
    lo = 0 if range[0] <= 0 else sums[range[0]-1]
    up = sums[-1] if range[1] >= len(nums) else sums[range[1]]
    print(range, "-->", up-lo)