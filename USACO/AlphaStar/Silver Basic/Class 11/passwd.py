L, C = map(int, input().split(" "))
letters = sorted(input().split(" "))
vowels = {'a', 'e', 'i', 'o', 'u'}

def recurse(i, pwd, hasVowels):
    global L, C, letters, vowels
    if len(pwd) == L:
        if hasVowels: print(pwd)
    else:
        for j in range(i, C):
            recurse(j+1, pwd+letters[j], hasVowels or letters[j] in vowels)

recurse(0, "", False)
