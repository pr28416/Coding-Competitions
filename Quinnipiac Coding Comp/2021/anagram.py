from collections import Counter

def ana_solve(words,N):
	count  = [list(word) for word in words]
	ordered = []
	for word in count:
		word.sort()
		ordered.append("".join(word))
	ordered.sort()
	pairs = 0
	intervals = []
	mini = 0
	for i in range(N):
		if ordered[i] != ordered[mini]:
			if i - mini > 1:
				intervals.append(i-mini)
			mini = i
		elif i == N-1:
			intervals.append(i+1-mini)
	for i in intervals:
		pairs += i*(i-1)*(i-2)/(3*2)
	return int(pairs)

	



T = int(input())
for _ in range(T):
	N = int(input())
	words = []
	for __ in range(N):
		words += [str(input())]
	print(ana_solve(words,N))
