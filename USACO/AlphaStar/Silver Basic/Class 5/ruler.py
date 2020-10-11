n = int(input())
def draw(n):
    if n > 1: draw(n-1)
    print("*"*n)
    if n > 1: draw(n-1)

print("*"*n)
draw(n-1)
print("*"*n)
