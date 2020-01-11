"""
ID: pranav.19
LANG: PYTHON3
TASK: palsquare
"""
base = 0
with open("palsquare.in", "r") as f:
    base = int(f.readline())

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def convert(b, n):
    new = ""
    number = n
    exp = 0
    while b**(exp+1) < number:
        exp += 1
    while exp >= 0:
        remainder = number % (b**exp)
        new += "0123456789ABCDEFGHIJK"[int(number//(b**exp))]
        number = remainder
        exp -= 1
    return new

output = ""
for n in range(1, 301):
    if isPalindrome(convert(base, n**2)):
        output += "%s %s\n" % (convert(base, n), convert(base, n**2))

with open("palsquare.out", "w") as f:
    f.write(output)
