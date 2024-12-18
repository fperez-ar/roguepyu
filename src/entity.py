from pygame import draw

# display related 
class Entity():
  def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.color = color
    self.rect = (x,y,width,height)

  def draw(self, win):
    draw.rect(win, self.color, self.rect)
  def get_pos(self):
    return self.x, self.y
  def update(self, **kwargs):
    pass