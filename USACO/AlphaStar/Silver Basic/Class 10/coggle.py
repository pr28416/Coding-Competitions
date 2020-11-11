class char:
    def __init__(self, ch, used=False):
        self.ch, self.used = ch, used
    def __str__(self): return self.__repr__()
    def __repr__(self): return self.ch

grid = [list(map(char, input().split(" "))) for _ in range(5)]

def crawl(grid, word, k, r, c):
    if len(word) == 0: return False
    if k == len(word): return True
    neighbors = [(i, j) for i in [-1, 0, 1] for j in [-1, 0, 1] if 0 <= r+i < len(grid) and 0 <= c+j < len(grid)]
    for (i, j) in neighbors:
        if not grid[r+i][c+j].used and grid[r+i][c+j].ch == word[k]:
            grid[r+i][c+j].used = True
            if crawl(grid, word, k+1, r+i, c+j):
                grid[r+i][c+j].used = False
                return True
            grid[r+i][c+j].used = False
    return False
        
def find(word, grid):
    for (i, j) in [(1, 1), (1, 3), (3, 1), (3, 3)]:
        if crawl(grid, word, 0, i, j):
            return 1
    return 0

s = 0
while True:
    try: e = input()
    except: break
    s += find(e, grid)
print(s)