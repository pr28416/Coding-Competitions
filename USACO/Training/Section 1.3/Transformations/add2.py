a = [2]
print(a)
def add2(x):
    a = x.copy()
    for i in range(len(a)):
        a[i] = a[i]+2
    
    return a

print (a, add2(a))
print(a)