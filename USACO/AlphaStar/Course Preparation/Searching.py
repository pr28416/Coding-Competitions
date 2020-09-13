def binSearch(lst, x, reverse=False):
    lo, up = 0, len(lst)
    while lo <= up:
        y = lo + (up - lo) // 2
        if lst[y] == x: return True
        if not reverse:
            if lst[y] > x: up = y-1
            else: lo = y+1
        else:
            if lst[y] < x: up = y-1
            else: lo = y+1
    return False

# Exercise 1.6
def ex1_6():
    print("Exercise 1.6")
    n, x = map(int, input().split(" "))
    lst = list(map(int, input().split(" ")))
    print("yes" if binSearch(lst, x) else "no")

# Exercise 1.7
def ex1_7():
    print("Exercise 1.7")
    n, x = input().split(" ")
    n = int(n)
    lst = list(input().split(" "))
    print("yes" if binSearch(lst, x, True) else "no")

def ex1_8():
    print("Exercise 1.8")
    n = int(input())
    x = sorted(list(map(int, input().split(" "))))
    y = sorted(list(map(int, input().split(" "))))
    i = j = 0
    common = []
    while i < len(x) and j < len(y):
        if x[i] == y[j]:
            common.append(x[i])
            i += 1; j += 1
        elif x[i] < y[j]: i += 1
        else: j += 1
    print(" ".join(map(str, common)))

ex1_8()