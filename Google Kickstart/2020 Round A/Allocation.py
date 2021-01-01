for T in range(int(input())):
    N, B = map(int, input().split(" "))
    houses = sorted(map(int, input().split(" ")))
    cost = count = 0
    for i in houses:
        if cost + i > B: break
        cost += i
        count += 1
    print(f"Case #{T+1}: {count}")