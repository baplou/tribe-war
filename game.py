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

from lib.coords import coords
from lib.screen_items import City
from lib.screen_items import Soldier
from lib.screen_items import Block

W, H = 1100, 850
screen = pygame.display.set_mode((W, H))
#pygame.display.set_icon()
clock = pygame.time.Clock()
soldiers = []
players = []
blocks = []
cities = [] # holds City() objects
cc = [] # city coords
        # for generate_cities()
green_block_image = pygame.transform.scale(pygame.image.load("assets/green-block.png"), (50, 50)).convert()
red_block_image = pygame.transform.scale(pygame.image.load("assets/red-block.png"), (50, 50)).convert()
house_image = pygame.transform.scale(pygame.image.load("assets/house.png"), (50, 50)).convert_alpha()

def generate_land():
  for i in coords:
    b = Block(random.choice([green_block_image, red_block_image]), i[0], i[1])
    blocks.append(b)

def generate_cities():
  valid = 0
  while valid <= 10:
    a = random.choice(coords)
    print(f"({a[0]}, {a[1]})")
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

# debugging
generate_land()
print("----- 1 -----")
generate_cities()
print("----- 2 -----")
for i in cities:
  print(f"({i.x}, {i.y})")

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
