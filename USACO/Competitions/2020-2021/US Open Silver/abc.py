import itertools

# [A, B, C, A+B, B+C, C+A, A+B+C]
pms = set()

def genPermutations(gen:list):
    if len(gen) >= 7:
        pms.add(tuple(gen))
    else:
        for i in range(len(gen)+1):
            gen.insert(i, None)
            genPermutations(gen)
            del gen[i]

genPermutations([4,5,6,7,8,9])
for i in pms: print(i)
# print(len(pms))

def solve(N, numbers):
    permutations = list(itertools.permutations(numbers))
    c = 0
    for pm in permutations:
        for i in range(3, 7):
            for j in range(3):
                if pm[i] != None and pm[j] != None and pm[i] <= pm[j]:
                    break
            else:
                continue
            break
        else:
            if pm[3] != None and pm[3] < 2: continue
            if pm[4] != None and pm[4] < 2: continue
            if pm[5] != None and pm[5] < 2: continue
            if pm[6] != None and pm[6] < 3: continue
            if pm[0] != None and pm[1] != None and pm[0] > pm[1]: continue
            if pm[0] != None and pm[2] != None and pm[0] > pm[2]: continue
            if pm[1] != None and pm[2] != None and pm[1] > pm[2]: continue
        continue

def run():
    T = int(input())
    for _ in range(T):
        N = int(input())
        numbers = list(map(int, input().split(" ")))
        print(numbers)
        for i in numbers:
            print(i)
        # for i in range(N-len(numbers)):
            # numbers.append(None)
        # solve(N, numbers)

# run()