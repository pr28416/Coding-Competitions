def unoptimizedFib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return unoptimizedFib(n-1)+unoptimizedFib(n-2)

def optimizedFib(n):
    # Problem: Takes exponential time
    existing = {
        0: 0,
        1: 1
    }
    existing = opFibHelp(n, existing)
    return existing
    
def opFibHelp(n, e):
    # Problem: Recursion depth exceeded
    if n-1 not in e.keys():
        e[n-1] = opFibHelp(n-1, e)
    
    if n-2 not in e.keys():
        e[n-2] = opFibHelp(n-2, e)

    return e[n-1]+e[n-2]

def evenMoreOptimizedFib(n):
    # No problem, 0(n)
    a, b, c = 0, 1, 1
    for i in range(n-1):
        c = a + b
        a, b = b, c
    return c

a = 10000000
print(evenMoreOptimizedFib(a))
# print(optimizedFib(a))
# print(unoptimizedFib(a))