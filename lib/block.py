# block.py
class Block:
  def __init__(self, image, x, y):
    self.image = image
    self.x = x
    self.y = y

  def draw(self, screen):
    screen.blit(self.image, (x, y))
