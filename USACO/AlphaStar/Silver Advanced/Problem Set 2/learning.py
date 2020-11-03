class Cow:
    def __init__(self, weight, spots):
        self.weight, self.spots = weight, int(spots == 1 or spots == "S")
    def __repr__(self): return self.__str__()
    def __str__(self): return f"(W:{self.weight}, S:{self.spots})"
    def __add__(self, other): return self.weight + other.weight

N, A, B = map(int, input().split(" "))
cows = []
for _ in range(N):
    t = input().split(" ")
    cows.append(Cow(int(t[1]), t[0]))
cows.sort(key=lambda x: x.weight)

intervals = []
for i in range(len(cows)):
    if not cows[i].spots: continue
    if i == 0: intervals.append([0, (cows[i]+cows[i+1])//2])
    elif i == len(cows)-1: intervals.append([(cows[i]+cows[i-1]+1)//2, 1000000001])
    else: intervals.append([(cows[i]+cows[i-1]+1)//2, (cows[i]+cows[i+1])//2])

i = 0
while i < len(intervals)-1:
    if intervals[i][1] >= intervals[i+1][0]:
        intervals[i][1] = intervals[i+1][1]
        del intervals[i+1]
    else: i += 1

a, b = 0, len(intervals)-1
while intervals[a][1] < A: a += 1
intervals[a][0] = max(intervals[a][0], A)
while intervals[b][0] > B: b -= 1
intervals[b][1] = min(intervals[b][1], B)

fin = 0
for i in range(a, b+1):fin += intervals[i][1]-intervals[i][0]+1

print(fin)