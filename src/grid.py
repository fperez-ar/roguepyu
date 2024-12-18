from pygame import draw
from math import floor

grid_color = (0, 0, 0) 

class Grid():
  def __init__(self, height: int, width: int, size: int):
    self.size = size
    self.row = floor(width / size)
    self.col = floor(height / size)
    self.grid = [[0 for _ in range(self.col)] for _ in range(self.row)]
    print('rows:', self.row)
    print('cols:', self.col)
    # print(self.grid)

  def _clamp(self, x, y):
    x = x if x >= 0 else len(self.grid)-1
    x = x if x < len(self.grid) else 0
    y = y if y >= 0 else len(self.grid[x])-1
    y = y if y < len(self.grid[x]) else 0
    return x,y

  def get(self, x: int, y: int):
    x, y  = self._clamp(int(x), int(y))
    print(x,y, len(self.grid), len(self.grid[x]))
    return self.grid[x][y]


  def set(self, new_pos: tuple[int,int], entity):
    ox, oy = entity.get_pos() # old pos
    nx, ny = self._clamp(new_pos[0], new_pos[1])
    grid_space = self.get(nx, ny)
    if grid_space == 0:
      self.grid[ox][oy] = 0
      entity.x = nx
      entity.y = ny
      self.grid[nx][ny] = entity


  def draw(self, win):
    for y in range(0, self.col):
      for x in range(0, self.row):
        coords = (x * self.size, y * self.size, self.size, self.size)
        draw.rect(win, grid_color, coords, 1)