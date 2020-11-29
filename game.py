#!/usr/bin/env python3
import random
import subprocess

try:
  import pygame
except ImportError:
  if input("Install the required dependencies? [y/n]: ") == "y":
    subprocess.run("pip3 install pygame", shell=True)

from lib.block import Block
from lib.screen_items import City
from lib.screen_items import Soldier
from lib.coords import coords

W, H = 1100, 850
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Tribe War")
clock = pygame.time.Clock()

soldiers = []
players = []
blocks = []

bg = pygame.transform.scale(pygame.image.load("assets/bg.png"), (W, H)).convert()
green_block_image = pygame.transform.scale(pygame.image.load("assets/green-block.png"), (50, 50)).convert()
red_block_image = pygame.transform.scale(pygame.image.load("assets/red-block.png"), (50, 50)).convert()

# todo:
# finish random land generation
# draw city images
# implement city functionality
# better land generation
# multiplayer support (noob networking)
def generate_land():
  for i in range(20):
    b = Block(green_block_image, (coords[random.choice(good_coords)], coords[random.choice(good_coords)]))
    blocks.append(b)

def redraw():
  # Screen Structure:
  # Layer 1 = Background (ocean)
  # Layer 2 = Land or "blocks"
  # Layer 3 = Charcters

  screen.blit(bg, (0,0))
  for block in blocks:
    block.draw(screen)
  for soldier in soldiers:
    soldier.draw(screen)

#generate_land()
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
