N = 0
order = []
with open("outofplace.in", "r") as f:
    N = int(f.readline())
    for i in range(N):
        order.append(int(f.readline()))

count = 0

correct = sorted(order)
# print(*order, " - original lineup")

while correct != order:
    bpos = 1
    for i in range(0, N):
        if i == N-1 and order[i] < order[i-1]:
            bpos = i
            break
        elif order[i] > order[i+1]:
            j = i
            while j-1 > 0 and order[j-1] == order[j]:
                j -= 1
            bpos = j
            break
    # if order[bpos] > order[bpos-1]: # Go right
    t = bpos+1
    while order[t] == order[bpos] and t + 1 < N:
        t += 1
    while t + 1 < N and order[t] == order[t+1]:
        t += 1
    order[bpos], order[t] = order[t], order[bpos]
    # print(*order)
    count += 1
        
    # else: # Go left

# print(*order, " - Final lineup")
# print("Count:", count)

# print("FINAL COUNT:", count)
with open("outofplace.out", "w") as f:
    f.write("%s\n" % count)