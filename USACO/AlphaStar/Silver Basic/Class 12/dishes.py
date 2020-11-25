N = int(input())
incoming = [i for i in range(N, 0, -1)]
washed, dried = [], []

while True:
    try:
        command = list(map(int, input().split(" ")))
    except:
        break
    if command[0] == 1:
        for _ in range(command[1]): washed.append(incoming.pop())
    else:
        for _ in range(command[1]): dried.append(washed.pop())

for i in range(len(dried)-1, -1, -1): print(dried[i])