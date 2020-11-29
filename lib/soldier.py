class Soldier:
  def __init__(self, x, y,  health=100):
    self.x = x
    self.y = y
    self.health = health

  def attack(self, other_character):
    other_character.health -= 50
