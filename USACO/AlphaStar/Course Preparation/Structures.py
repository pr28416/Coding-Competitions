# Exercise 1.5
def ex1_5():
    print("Exercise 1.5")
    n = int(input())
    lst = [list(map(int, input().split(" "))) for _ in range(n)]
    lst.sort(key=lambda x: (x[1] // 10) % 10)
    lst.sort(key=lambda x: x[0] % 10)
    for i in lst:
        print(*i)

ex1_5()