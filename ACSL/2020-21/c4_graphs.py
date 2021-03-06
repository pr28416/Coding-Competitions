def sumPathsOfLength2(edges):
    paths = [None] * 11
    line = list(map(int, edges.strip(" ").split(" ")))
    for i in line:
        if paths[i // 10] == None: paths[i // 10] = set()
        paths[i // 10].add(i % 10)

    fin = 0
    for a, al in enumerate(paths):
        if al == None: continue
        for b in al:
            if paths[b] == None: continue
            for c in paths[b]:
                if a == b or a == c or b == c: continue
                fin += 100*a + 10*b + c
    return fin


print(sumPathsOfLength2("12 23 34 41 31"))
print(sumPathsOfLength2("12 23 34 41 13 32"))
print(sumPathsOfLength2("76 75 12 13 23 31 34 41 56"))
