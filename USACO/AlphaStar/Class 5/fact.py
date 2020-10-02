n = int(input())
f = lambda x: 1 if x <= 1 else x*f(x-1)
print(f(n))