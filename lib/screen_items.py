# screen_items.py
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
  def __init__(self, level=1):
    self.level = level
