import sys
sys.setrecursionlimit(40000)
def rec(n):
    if n == 8394:
        return n
    else:
        return rec(n+1);

print(rec(0))