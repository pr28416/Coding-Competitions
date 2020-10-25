N = int(input())

def isPrime(x):
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x % 3 == 0 or x < 2: return False
    else:
        for i in range(3, min(int(x**0.5)+1, x), 2):
            if x % i == 0: return False
    return True

def recurse(x, l):
    global N
    if l == N: print(x)
    else:
        for i in [1, 3, 5, 7, 9]:
            if isPrime(x*10+i):
                recurse(x*10+i, l+1)

for i in [2, 3, 5, 7]:
    recurse(i, 1)
