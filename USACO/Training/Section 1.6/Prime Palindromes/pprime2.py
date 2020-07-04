"""
ID: pranav.19
LANG: PYTHON3
TASK: pprime
"""

from datetime import datetime
start = datetime.now()

def time():
    print(datetime.now()-start)

a, b = 0, 0
with open("pprime.in", "r") as f:
    temp = f.readline().split(" ")
    a, b = int(temp[0]), int(temp[1])

# print(a, b)

def isPalindrome(n):
    n = str(n)
    for i in range(int(len(n)/2)+1):
        if n[i] != n[len(n)-1-i]:
            return False
    return True

# Get max palindrome
maxPalindrome = b
while not isPalindrome(maxPalindrome):
    maxPalindrome -= 1

# print(maxPalindrome)

def isPrime(n):
    if n % 2 == 0 or n % 3 == 0 or n < 5:
        return False
    else:
        for i in range(3, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True


palindromes = []

def makePalindrome(current):
    """
    # Iterate through digits
    for i in range(10):
        # print(i, current)
        # Check if current is not currently a number
        if len(current) == 0:
            # If so, add the number first
            current = str(i)
            # Check if number is in palindromes
            if int(current) not in palindromes and isPrime(int(current)):
                palindromes.append(int(current))
                # print(current)

            makePalindrome(current)
            current = current[0:len(current)-1]
        else:
        """
    # Make sure length of potential palindrome is less than the maxPalindrome
    if int(current) <= int(str(maxPalindrome)[0:len(str(maxPalindrome)) // 2 + 1]) and len(current) <= (len(str(maxPalindrome))+1)//2:

        if current[0] not in ["0", "2", "4", "5", "6", "8"]:
            String = current
            # Make an odd-number-of-digits palindrome and add it
            oddPalindrome = int(String + String[len(String)-2::-1])

            # Check if number is in palindromes
            if oddPalindrome not in palindromes and isPrime(int(oddPalindrome)) and int(oddPalindrome) >= a:
                palindromes.append(oddPalindrome)
                # print("Adding odd palindrome: %s" % (String + String[len(String)-2::-1]))

            # Make an even-number-of-digits palindrome and add it
            evenPalindrome = int(String + String[len(String)-1::-1])
            # print(evenPalindrome)

            # Check if number is in palindromes - DO WE NEED EVEN-DIGIT PALINDROMES?
            if evenPalindrome not in palindromes and isPrime(int(evenPalindrome)) and int(evenPalindrome) >= a:
                palindromes.append(evenPalindrome)
                # print("Adding even palindrome: %s" % (String + String[len(String)-1::-1]))



            for i in range(10):
                makePalindrome(current+str(i))

for i in [5, 7]:
    if i >= a:
        palindromes.append(i)

for i in [1, 3, 7, 9]:
    makePalindrome(str(i))

palindromes.sort()
# print(palindromes)
# time()
with open("pprime.out", "w") as f:
    for i in palindromes:
        f.write("%s\n" % i)