from datetime import datetime
start = datetime.now()

a, b = 0, 0
with open("pprime.in", "r") as f:
    temp = f.readline().split(" ")
    a, b = int(temp[0]), int(temp[1])

print(a, b)

def isPalindrome(n):
    n = str(n)
    for i in range(int(len(n)/2)+1):
        if n[i] != n[len(n)-1-i]:
            return False
    return True

def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n < 2:
        return False
    else:
        for i in range(3, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

def time():
    print(datetime.now()-start)

# Get max palindrome
maxPalindrome = b
while not isPalindrome(maxPalindrome):
    maxPalindrome -= 1

print(maxPalindrome)

time()

def makePalindrome(givenSegment):
    if len(givenSegment) == (len(str(maxPalindrome))+1)//2:
        print(str(givenSegment), end=", ")
        p1 = int(givenSegment)
        temp = ""
        for i in range()
    else:
        for i in range(10):
            givenSegment += str(i)
            makePalindrome(givenSegment)
            givenSegment = givenSegment[:len(givenSegment)-1]

makePalindrome("")