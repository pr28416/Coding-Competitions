st, en, tl1, tl2 = 0, 0, 0, 0
with open("teleport.in", "r") as f:
    st, en, tl1, tl2 = (int(i) for i in f.readline().split(" "))
    # print(st, en, tl1, tl2)

minimum = min(abs(en - st), abs(st - tl1) + abs(en - tl2), abs(st - tl2) + abs(en - tl1))
with open("teleport.out", "w") as f:
    f.write("%s\n" % minimum)