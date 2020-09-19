M, N = map(int, input().split(" "))
phrases = [input() for _ in range(M)]
queries = [input() for _ in range(N)]

def binSearch(lst, x):
    lo, up = 0, len(lst)
    while lo < up:
        y = lo+(up-lo)//2
        if x <= lst[y]: up=y
        else: lo=y+1
    return lo

phrases.sort()

count = 0
for query in queries:
    index = min(binSearch(phrases, query), len(phrases)-1)
    if phrases[index][:len(query)] == query: count += 1
print(count)
