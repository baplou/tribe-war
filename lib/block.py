# block.py
class Block:
  def __init__(self, image, x, y):
    self.image = image
    self.x = x
    self.y = y

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

  def __repr__(self):
    return f"[block: x={self.x} y={self.y}"
