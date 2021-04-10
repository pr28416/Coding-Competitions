def solve(lst):
    total = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]: continue
        origlen = len(str(lst[i]))
        old = lst[i]
        # n = 0
        # while len(str(lst[i])) < len(str(lst[i-1])) and :
        # while len(str(lst[i])) < len(str(lst[i-1])):
        #     lst[i] *= 10
        # # while lst[i] > lst[i-1]:
        # #     if str(lst[i])[0] != str(lst[i]-1)[0]: break
        # #     lst[i] -= 1
        # while lst[i] <= lst[i-1]:
        #     if str(lst[i])[0] != str(lst[i]+1)[0]:
        #         # lst[i] = int(str(lst[i])[0]) * (len(str(lst[i])))
        #         lst[i] = old
        #         while lst[i] <= lst[i-1]:
        #             lst[i] *= 10
        #         break
        #     lst[i] += 1


        numExtras = 1

        while True:
            lst[i] = old * 10**numExtras
            # print(lst[i])
            if len(str(lst[i])) < len(str(lst[i-1])):
                numExtras += 1
                continue
            lo, up = lst[i], int(str(old)+"9"*numExtras)+1
            oldup = up
            # while int(str(lst[i])[:origlen]) == old:
                # if lst[i] > lst[i-1]:
                    # print("broke")
                    # break
                # lst[i] += 1
            # else:
                # numExtras += 1
                # continue
            # break
            while lo < up:
                lst[i] = (lo+up)//2
                if lst[i] > lst[i-1]: up = lst[i]
                else: lo=lst[i]+1
            lst[i] = lo
            if lst[i] >= oldup: numExtras += 1
            elif lst[i] > lst[i-1]: break
            else: numExtras += 1

        total += len(str(lst[i]))-origlen
    # print(lst)
    return total

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split(" ")))
    ans = solve(lst)
    print(f"Case #{t}: {ans}")