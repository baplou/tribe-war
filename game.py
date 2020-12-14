#!/usr/bin/env python3
import random
import subprocess

try:
  import pygame
except ImportError:
  if input("Install the required dependencies? [y/n]: ") == "y":
    subprocess.run("pip3 install pygame", shell=True)
  else:
    quit()

from lib import coords
from lib import City
from lib import Soldier
from lib import Block
from lib import Cursor

W, H = 1100, 850
screen = pygame.display.set_mode((W, H))
#pygame.display.set_icon()
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

soldiers = []
players = []
blocks = []
cities = [] # holds City() objects
cc = []     # city coords
            # for generate_cities()

green_block_image = pygame.transform.scale(pygame.image.load("assets/green-block.png"), (50, 50)).convert()
red_block_image = pygame.transform.scale(pygame.image.load("assets/red-block.png"), (50, 50)).convert()
house_image = pygame.transform.scale(pygame.image.load("assets/house.png"), (50, 50)).convert_alpha()
cursor_image = pygame.transform.scale(pygame.image.load("assets/cursor.png"), (40, 40)).convert_alpha()

# object used to display special cursor
cursor = Cursor(cursor_image, (0, 0))

def generate_land():
  for i in coords:
    b = Block(random.choice([green_block_image, red_block_image]), i[0], i[1])
    blocks.append(b)

def generate_cities():
  valid = 0
  while valid <= 10:
    a = random.choice(coords)
    if len(cc) == 0:
      cc.append(a) 
      ret = City(a[0], a[1], house_image)
      cities.append(ret)
      valid += 1
    else:
      for i in cc:
        if a != i:
          cc.append(a) 
          ret = City(a[0], a[1], house_image)
          cities.append(ret)
          valid += 1
          break

generate_land()
generate_cities()

red_house_image = pygame.transform.scale(pygame.image.load("assets/red-house.png"), (50, 50)).convert_alpha()
green_house_image = pygame.transform.scale(pygame.image.load("assets/green-house.png"), (50, 50)).convert_alpha()

def choose_color_city(img):
  ret = random.choice(cities)
  cities.remove(ret)
  ret.image = img
  return ret

red_cities = [choose_color_city(red_house_image)]
green_cities = [choose_color_city(green_house_image)]

def redraw():
  # Screen Structure:
  # Layer 1 = Land or "blocks"
  # Layer 2 = City
  # Layer 3 = Soldier
  for block in blocks:
    block.draw(screen)
  for soldier in soldiers:
    soldier.draw(screen)
  for city in cities:
    city.draw(screen)
  for c in red_cities:
    c.draw(screen)
  for c in green_cities:
    c.draw(screen)
  cursor.draw(screen)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()
    elif event.type == pygame.MOUSEMOTION:
      # so collision detection
      # will not be messed up
      # in the future.
      cursor.coord = event.pos
    elif event.type == pygame.MOUSEBUTTONDOWN:
      print(cursor.coord)

  for soldier in soldiers:
    if soldier.health <= 0:
      soldiers.remove(soldier)

  redraw()

  pygame.display.update()
  clock.tick(60)
