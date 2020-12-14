class Soldier:
  def __init__(self, x, y, image, health=100):
    self.x = x
    self.y = y
    self.image = image
    self.health = health
    self.moved = False
    self.kills = 0

  def attack(self, other_character):
    other_character.health -= 50

  def update(self):
    if self.kills == 5:
      self.health = 200

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

class City:
  def __init__(self, x, y, image, level=1):
    self.x = x
    self.y = y
    self.image = image
    self.level = level

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

class Block:
  def __init__(self, image, x, y):
    self.image = image
    self.x = x
    self.y = y

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

  def __repr__(self):
    return f"[block: x={self.x} y={self.y}"

class Cursor:
  def __init__(self, image, coord):
    self.image = image
    self.coord = coord

  def draw(self, screen):
    screen.blit(self.image, self.coord)
