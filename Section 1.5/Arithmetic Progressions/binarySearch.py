def binarySearch(e, x):
    low, up = 0, len(x)-1
    while len(x[low:up]) > 1:
        print(x[low:up+1])
        mid = int((up+low)/2)
        if e == x[mid]:
            return mid
        elif e < x[mid]:
            up = mid
        else:
            low = mid
    if len(x[low:up]) == 1:
        print(x[low:up+1])
        return int((up+low)/2)

data = [i for i in range(1, 101)]
n = 111
print(binarySearch(n, data))