"""
ID: pranav.19
LANG: PYTHON3
TASK: sprime
"""

N = 0
with open("sprime.in", "r") as f:
    N = int(f.readline())

def isPrime(n):
    if n == 2 or n == 3: return True
    elif n % 2 == 0 or n % 3 == 0 or n < 2: return False
    else:
        for i in range(3, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

superprimes = []

def addOn(currentStr):
    if len(currentStr) == N:
        superprimes.append(currentStr)
    else:
        for i in [1, 3, 7, 9]:
            if isPrime(int(currentStr+str(i))):
                addOn(currentStr+str(i))


for i in [2, 3, 5, 7]:
    addOn(str(i))

with open("sprime.out", "w") as f:
    for i in superprimes:
        f.write("%s\n" % i)