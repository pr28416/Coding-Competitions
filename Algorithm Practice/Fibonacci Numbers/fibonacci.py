def unoptimizedFib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return unoptimizedFib(n-1)+unoptimizedFib(n-2)

print(unoptimizedFib(100))