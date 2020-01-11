"""
ID: pranav.19
LANG: PYTHON3
TASK: milk
"""
totalMilk = 0
vendorInfo = []
totalPay = 0

with open("milk.in", "r") as f:
    firstLine = f.readline().split(" ")
    totalMilk = int(firstLine[0])
    for i in range(int(firstLine[1])):
        temp = f.readline().split(" ")
        vendorInfo.append([int(temp[0]), int(temp[1])])

# Merge sort
def split(x):
    if len(x) == 1:
        return x
    else:
        a = split(x[0:int(len(x)/2)])
        b = split(x[int(len(x)/2):])
        return merge(a, b)
    
def merge(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][0] < b[0][0]:
            x.append(a.pop(0))
        else:
            x.append(b.pop(0))
    while len(a) > 0:
        x.append(a.pop(0))
    while len(b) > 0:
        x.append(b.pop(0))
    return x

# --------
if totalMilk != 0:
    vendorInfo = split(vendorInfo)
    # for i in vendorInfo:
    #     print(i)
    for vendor in vendorInfo:
        # print(vendor)
        if vendor[1] <= totalMilk:
            # print("Amount taken: {}".format(vendor[1]))
            totalMilk -= vendor[1]
            totalPay += vendor[0]*vendor[1]
        else:
            amt = vendor[1]
            while amt > totalMilk:
                amt -= 1
            # print("Amount taken: {}".format(amt))
            totalMilk -= amt
            totalPay += vendor[0]*amt
        # print("Remaining milk needed: {}".format(totalMilk))
        if totalMilk == 0:
            break

with open("milk.out", "w") as f:
    f.write("{}\n".format(totalPay))