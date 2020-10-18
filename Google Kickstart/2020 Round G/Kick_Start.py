T = int(input())
for s in range(T):
    string = input()
    track = []
    i = 0
    while i < len(string):
        if string[i:i+5] == "START":
            track.append(1)
            # i += 5
        elif string[i:i+4] == "KICK":
            track.append(0)
            # i += 4
        # else: i += 1
        i += 1
    # print(track)
    oneCount = 0
    finCount = 0
    for j in range(len(track)-1, -1, -1):
        if track[j] == 1: oneCount += 1
        else: finCount += oneCount
    print("Case #%s: %s" % (s+1, finCount))