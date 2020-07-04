"""
ID: pranav.19
LANG: PYTHON3
TASK: ariprog
"""

import time
start = time.time()

N, M = 0, 0
with open("ariprog5.in", "r") as f:
    N = int(f.readline())
    M = int(f.readline())

bisquares = []
print("Generating bisquares")
for p in range(M+1):
    for q in range(M+1):
        if p**2+q**2 not in bisquares:
            bisquares.append(p**2+q**2)

print("Initial sort")
bisquares.sort()
answers = []
print(bisquares)
print("It took", time.time()-start, "seconds.")
print("Started solving")

def binaryFind(e, x):
    low, up = 0, len(x)-1
    while len(x[low:up]) > 1:
        mid = int((up+low)/2)
        if e == x[mid]:
            return mid
        elif e < x[mid]:
            up = mid
        else:
            low = mid
    if len(x[low:up]) == 1:
        return int((up+low)/2)

cycles = 0
for i1 in range(len(bisquares)-1):
    # print("A: b =", b)
    b = bisquares[i1]
    if b + 2*(bisquares[i1+1]-b) <= bisquares[len(bisquares)-1]:
        for c in range(len(bisquares[i1+1:])):
            incrementer = bisquares[c]-b
            # print("\tB: incrementer =", incrementer)
            if (b+2*incrementer in bisquares[c+1:]):
                if bisquares[len(bisquares)-1]-(b+incrementer*(N-1)) >= 0:
                    counter = 3
                    keepGoing = True
                    while keepGoing and counter < N:
                        # print("\t\tC: counter =", counter)
                        cycles += 1
                        keepGoing = False
                        if b+incrementer*counter in bisquares[c+1:]:
                            keepGoing = True
                            counter += 1
                    # print(b, incrementer, counter)
                    if counter == N:
                        answers.append([b, incrementer])
                else:
                    break
    else:
        break


# for(i1, b) in enumerate(bisquares[:len(bisquares)-1]):
#     if b + 2*(bisquares[i1+1]-b) <= bisquares[len(bisquares)-1]:
#         for (i2, c) in enumerate(bisquares[i1+1:]):
#             incrementer = c-b
#             if b+2*incrementer in bisquares:
#                 if bisquares[len(bisquares)-1]-(b+incrementer*(N-1)) >= 0:
#                     counter = 3
#                     keepGoing = True
#                     while keepGoing and counter < N:
#                         cycles += 1
#                         keepGoing = False
#                         if b+incrementer*counter in bisquares[i1:]:
#                             keepGoing = True
#                             counter += 1
#                     if counter == N:
#                         answers.append([b, incrementer])
#                 else:
#                     break
#     else:
#         break


# def alg2():
# cycles = 0
# for(i1, b) in enumerate(bisquares[:len(bisquares)-1]):
#     if b + 2*(bisquares[i1+1]-b) <= bisquares[len(bisquares)-1]:
#         for (i2, c) in enumerate(bisquares[i1+1:]):
#             incrementer = c-b
#             if b+2*incrementer in bisquares:
#                 if bisquares[len(bisquares)-1]-(b+incrementer*(N-1)) >= 0:

#                     counter = 1
#                     checkingIdx = i2+1

#                     while checkingIdx < len(bisquares) and counter < N:
#                         cycles += 1
#                         # Keep going if less than or equal to, otherwise stop
#                         if bisquares[checkingIdx] == b+incrementer*counter:
#                             counter += 1
#                             checkingIdx += 1
#                         elif bisquares[checkingIdx] < b+incrementer*counter:
#                             checkingIdx += 1
#                         else:
#                             break
#                     if counter == N:
#                         answers.append([b, incrementer])
#                 else:
#                     break
#     else:
#         break

         
# print(len(bisquares))
# cycles = alg1()

print("Finished solving")
print(answers)

def split(n):
    if len(n) == 1:
        return n
    else:
        half = int(len(n)/2)
        a = split(n[0:half])
        b = split(n[half:len(n)])
        return merge(a, b)

def merge(a, b):
    x = []
    while len(a) > 0 and len(b) > 0:
        if a[0][1] < b[0][1]:
            x.append(a.pop(0))
        elif a[0][1] > b[0][1]:
            x.append(b.pop(0))
        else:
            if a[0][0] < b[0][0]:
                x.append(a.pop(0))
            else:
                x.append(b.pop(0))
    while len(a) > 0:
        x.append(a.pop(0))
    while len(b) > 0:
        x.append(b.pop(0))
    return x

valuesAreThere = True
print("It took", time.time()-start, "seconds.")
print("Starting merge sort")
if len(answers) == 0:
    valuesAreThere = False
else:
    answers = split(answers)
print("Finished merge sort")

with open("ariprog.out", "w") as f:
    if valuesAreThere:
        for i in answers:
            f.write("%s %s\n" % (i[0], i[1]))
    else:
        f.write("NONE\n")

print("It took", time.time()-start, "seconds.")
print("%s cycles" % cycles)