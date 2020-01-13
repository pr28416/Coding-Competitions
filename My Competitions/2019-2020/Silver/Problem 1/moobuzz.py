N = 0
with open("moobuzz.in", "r") as f:
    N = int(f.readline())

a = [1, 2, 4, 7, 8, 11, 13, 14]
x = [8, 1, 2, 3, 4, 5, 6, 7]
c = (N-x[N%8])//8
b = a[N%8-1]+15*(c)

with open("moobuzz.out", "w") as f:
    f.write("%s\n" % b)
