with open('rental.in') as f:
    N, M, R = map(int, f.readline().split(" "))
    milkCapacity = sorted([int(f.readline()) for _ in range(N)], reverse=True)
    stores = sorted([list(map(int, f.readline().split(" "))) for _ in range(M)], key=lambda x: x[1])
    rent = sorted([int(f.readline()) for _ in range(R)], reverse=True)

print(N, M, R)
print('mc:', milkCapacity)
print('stores:')
for i in stores:
    print(i)
print('rent:', rent)

results = [0] * N
for k in range(N+1):
    # rent: k, store: n-k
    # rent
    money = 0
    for i in range(min(R, k)):
        money += rent[i] * milkCapacity[i]
    


"""

case 1: 5 store, 0 rent

7: 25*7=175
6: 25*3+15*3=120
5: 

case 2: 4 store, 1 rent



case 2: 3 store, 2 rent



case 2: 2 store, 3 rent



case 2: 1 store, 4 rent



case 2: 0 store, 5 rent



"""