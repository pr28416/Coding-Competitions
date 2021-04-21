def solve(R, C, message):
	c = 0
	i, j = 0, 0
	grid = [[0] * C for _ in range(R)]
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	dirIdx = 0
	pi, pj = 0, 0
	for _ in range(R*C):
		# print(i, j)
		# Set mark
		grid[i][j] = message[c]
		c = (c+1)%len(message)
		# Move
		nr, nc = i+directions[dirIdx][0], j+directions[dirIdx][1]
		if nr >= R or nc >= C or grid[nr][nc] != 0:
			# Change direction
			dirIdx = (dirIdx + 1) % 4
		pi, pj = i, j
		i, j = i+directions[dirIdx][0], j+directions[dirIdx][1]
	# for v in grid:
		# print(*v)
	return grid[pi][pj]

T = int(input())
for _ in range(T):
	R, C = map(int, input().split(" "))
	message = input()
	print(solve(R, C, message))
