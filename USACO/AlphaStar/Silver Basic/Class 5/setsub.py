n = int(input())
numbers = input().split(" ")

from queue import Queue
qu = Queue()
qu.put(["", -1])

while not qu.empty():
    val = qu.get_nowait()
    if val[0]: print(val[0])
    for i in range(val[1]+1, len(numbers)):
        val[0] += numbers[i]
        qu.put([val[0], i])
        val[0] = val[0][:-1]