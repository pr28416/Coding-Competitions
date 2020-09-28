N = int(input())
guesses = [tuple(input().split(" ")) for _ in range(N)]

def check(secret, guesses):
    for guess in guesses:
        # Check for correct digits in correct location
        count = 0
        usedSecret = [1] * 4
        usedGuess = [1] * 4
        for d in range(4):
            if secret[d] == guess[0][d]:
                count += 1
                usedSecret[d] = usedGuess[d] = 0
        if str(count) != guess[1]: return False
        # Check for correct digits in wrong location
        count = 0
        for i in range(4):
            if not usedSecret[i]: continue
            usedSecret[i] = 0
            for j in range(4):
                if not usedGuess[j]: continue
                if secret[i] == guess[0][j]:
                    count += 1
                    usedGuess[j] = 0
                    break
        if str(count) != guess[2]: return False
    return True

for number in range(1000, 10000):
    if check(str(number), guesses):
        print(number)
        break
else:
    print("NONE")