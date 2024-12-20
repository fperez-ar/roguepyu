from pygame import draw

# display related 
class Entity():
  # width: int, height: int
  def __init__(self, x: int, y: int, size: int, color: tuple):
    self.x = x
    self.y = y
    self.width = size
    self.height = size
    self.color = color
    self.rect = (x, y, size, size)
    self.name = ''

  def draw(self, win):
    draw.rect(win, self.color, self.rect)
  def set_pos(self, x: int, y: int):
    self.x = x
    self.y = y
  def get_pos(self):
    return self.x, self.y
  def update(self, **kwargs):
    x = self.x * self.width
    y = self.y * self.height
    self.rect = (x, y, self.width, self.height)