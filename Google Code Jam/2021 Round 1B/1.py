def solve(string):
    lst = [0] * len(string)
    lst[0] = 1
    for i in range(1, len(string)):
        if string[i] > string[i-1]:
            lst[i] = lst[i-1]+1
        else:
            lst[i] = 1
    return lst


T = int(input())
for t in range(1, T+1):
    N = int(input())
    string = input()
    print(f"Case #{t}:", *solve(string))