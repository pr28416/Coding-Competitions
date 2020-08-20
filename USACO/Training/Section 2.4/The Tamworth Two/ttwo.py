"""
ID: pranav.19
LANG: PYTHON3
TASK: ttwo
"""

grid = None

with open("ttwo.in", "r") as f:
    grid = list(map(lambda x: list(x.strip("\n")), f.readlines()))


class Position:
    def __init__(self, grid, x, y, d='n'):
        self.x, self.y, self.d = x, y, d
        self.grid = grid

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def move(self):
        if self.d == 'n':
            if self.y == 0 or self.grid[self.y-1][self.x] == '*':
                self.d = 'e'
            else:
                self.y -= 1
        elif self.d == 's':
            if self.y == 9 or self.grid[self.y+1][self.x] == '*':
                self.d = 'w'
            else:
                self.y += 1
        elif self.d == 'e':
            if self.x == 9 or self.grid[self.y][self.x+1] == '*':
                self.d = 's'
            else:
                self.x += 1
        else: # self.d == 'w'
            if self.x == 0 or self.grid[self.y][self.x-1] == '*':
                self.d = 'n'
            else:
                self.x -= 1


cow, farmer = None, None
for i in range(len(grid)):
    for j in range(len(grid)):
        if grid[i][j] == 'C': cow = Position(grid, j, i)
        if grid[i][j] == 'F': farmer = Position(grid, j, i)

minutes = 0
while minutes < 160000:
    minutes += 1
    cow.move()
    farmer.move()
    if cow == farmer: break
else:
    minutes = 0

with open("ttwo.out", 'w') as f:
    f.write(f"{minutes}\n")