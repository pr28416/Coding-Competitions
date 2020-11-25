N = int(input())
lines = [input().split(" ") for _ in range(N)]
for a in lines:
    p, c = a[1], 0
    # print(p)
    sk = []
    for i in p:
        if i == ">": sk.append(i)
        elif len(sk) == 0:
            print("illegal");
            break
        else: sk.pop()
    else:
        # print(sk)
        print("illegal" if len(sk) != 0 else "legal")
