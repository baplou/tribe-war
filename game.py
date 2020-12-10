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
bg = pygame.transform.scale(pygame.image.load("assets/bg.png"), (W, H)).convert()
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
def generate_cities():
  a = random.choice(coords)
  cc.append(coords.index(a))
  if len(cc) == 1:
    pass
  else:
    # compare to see if cities are too close
    # try:
    #   coords.index(a)
    pass
    #ret = City(a[0], a[1] """image""")
    #cities.append(ret)

def redraw():
  # Screen Structure:
  # Layer 1 = Background (ocean)
  # Layer 2 = Land or "blocks"
  # Layer 3 = City
  # Layer 4 = Soldier
  screen.blit(bg, (0,0)) # not necessary
  for block in blocks:
    block.draw(screen)
  for soldier in soldiers:
    soldier.draw(screen)

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
