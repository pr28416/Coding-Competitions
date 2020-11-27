for k in range(5):
    s, d, r = map(int, input().split(" "))
    s, d = int(f"0o{s}", 8), int(f"0o{d}", 8)
    n = (r-1)*r//2+1
    fin = 0
    for i in range(n, n+r):
        a = oct(s+d*(i-1))
        for i in range(2, len(a)):
            fin += int(a[i])
    print(f"{k+1}. {fin}")