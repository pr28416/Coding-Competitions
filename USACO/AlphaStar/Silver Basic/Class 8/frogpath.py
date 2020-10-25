path = [int(i == "-") for i in input()]
# print(path)
total = 0

def recurse(path, i):
    global total
    if i >= len(path)-1:
        total += 1
    else:
        if path[i+1]: recurse(path, i+1)
        if i+2 <= len(path)-1 and path[i+2]: recurse(path, i+2)

recurse(path, 0)
print(total)