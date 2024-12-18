from entity import Entity

class Player(Entity):
  # def __init__(self, x: int, y: int, width: int, height: int, color: tuple):
  #   super().__init__(x, y, width, height, color)  
  # def draw(self, win):
  #   super().draw(win)
  def update(self, **kwargs):
    grid = kwargs.get('grid')
    x = self.x * grid.size
    y = self.y * grid.size
    self.rect = (x, y, self.width, self.height)

