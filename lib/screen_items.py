import pygame

class Soldier:
  def __init__(self, x, y, image, health=100):
    self.x = x
    self.y = y
    self.image = image
    self.health = health
    self.moved = False
    self.kills = 0
    self.mask = pygame.mask.from_surface(self.image)
    self.selected = False

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
    self.mask = pygame.mask.from_surface(self.image)
    self.selected = False

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

class Block:
  def __init__(self, image, x, y):
    self.image = image
    self.x = x
    self.y = y
    self.mask = pygame.mask.from_surface(self.image)

  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))

  def __repr__(self):
    return f"[block: x={self.x} y={self.y}"

class Cursor:
  def __init__(self, image, coord):
    self.image = image
    self.coord = coord
    self.mask = pygame.mask.from_surface(self.image)

  def draw(self, screen):
    screen.blit(self.image, self.coord)

class NextTurn:
  def __init__(self):
    self.image = pygame.transform.scale(pygame.image.load("assets/next_turn.png"), (100, 100)).convert_alpha()
    self.coord = (990, 845)
    self.x = self.coord[0]
    self.y = self.coord[1]
    self.mask = pygame.mask.from_surface(self.image)
