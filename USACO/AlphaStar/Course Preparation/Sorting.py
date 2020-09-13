def selectionSort(lst, start: int=None, end: int=None, reverse=False):
    if start is None: start = 0
    if end is None: end = len(lst)
    print(f"outer: start={start}, end={end}")
    for i in range(start, end):
        print("inner")
        for j in range(i+1, end):
            if not reverse and lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                print('swap')
            elif reverse and lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                print('swap')

# Exercise 1.1
def ex1_1():
    print("Exercise 1.1")
    n = int(input())
    lst = list(map(int, input().split(" ")))
    selectionSort(lst)
    print(" ".join(map(str, lst)))

# Exercise 1.2
def ex1_2():
    print("Exercise 1.2")
    n = int(input())
    string = input().split(" ")
    selectionSort(string, reverse=True)
    print(" ".join(string))

# Exercise 1.3
def ex1_3():
    print("Exercise 1.3")
    n, x, y = map(int, input().split(" "))
    lst = list(map(int, input().split(" ")))
    selectionSort(lst, x, y)
    print(" ".join(map(str, lst)))

# Exercise 1.4
def ex1_4():
    print("Exercise 1.4")
    n = int(input())
    x = list(map(int, input().split(" ")))
    y = list(map(int, input().split(" ")))
    ans = []
    while len(x) > 0 and len(y) > 0:
        if x[-1] > y[-1]: ans.append(x.pop())
        else: ans.append(y.pop())
    while len(x) > 0: ans.append(x.pop())
    while len(y) > 0: ans.append(y.pop())
    ans = reversed(ans)
    print(" ".join(map(str, ans)))

ex1_4()