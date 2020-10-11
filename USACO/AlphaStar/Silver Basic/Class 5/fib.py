i = int(input())
a, b, c = 1, 0, 0
for j in range(i):
    c = a+b
    a = b
    b = c
print(c)