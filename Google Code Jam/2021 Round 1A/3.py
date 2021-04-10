T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split(" "))
    papers = []
    maxIdx = 0
    for i in range(N):
        line = input().split(" ")
        papers.append((line[0], int(line[1])))
        if int(line[1]) > papers[maxIdx][1]:
            maxIdx = i
    print(f"Case #{t}: {papers[maxIdx][0]} {papers[maxIdx][1]}/1")
    