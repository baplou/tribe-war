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

from lib.block import Block
from lib.screen_items import City
from lib.screen_items import Soldier
from lib.coords import coords

# var and const
W, H = 1100, 850
screen = pygame.display.set_mode((W, H))
#pygame.display.set_icon()
clock = pygame.time.Clock()
soldiers = []
players = []
blocks = []
cities = []
cc = [] # city coords
        # for generate_cities()
green_block_image = pygame.transform.scale(pygame.image.load("assets/green-block.png"), (50, 50)).convert()
red_block_image = pygame.transform.scale(pygame.image.load("assets/red-block.png"), (50, 50)).convert()

# todo:
# draw city images
# implement city functionality
# multiplayer support (noob networking)
# ocean
def generate_land():
  for i in coords:
    b = Block(random.choice([green_block_image, red_block_image]), i[0], i[1])
    blocks.append(b)

# not working yet
# need to draw cities
def generate_cities():
  while valid < 15:
    a = random.choice(coords)
    if len(cc) == 1:
      cc.append(a) 
      #ret = City(a[0], a[1] """image""")
      #cities.append(ret)
      valid += 1
    else:
      for c in cc:
        if abs(c[0] - a[0]) >= 500 and abs(c[1] - a[1]) >= 500: # compare if cities are too close
          valid += 1
          #ret = City(a[0], a[1] """image""")
          #cities.append(ret)

def redraw():
  # Screen Structure:
  # Layer 1 = Land or "blocks"
  # Layer 2 = City
  # Layer 3 = Soldier
  for block in blocks:
    block.draw(screen)
  for soldier in soldiers:
    soldier.draw(screen)
  """
  for city in cities:
    city.draw(screen)
  """

generate_land()
#generate_cities()
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  for soldier in soldiers:
    if soldier.health <= 0:
      soldiers.remove(soldier)

  redraw()

  pygame.display.update()
  clock.tick(60)
