#!/usr/bin/env python3
import subprocess
import pygame
import random
from lib import *

turn = "green"
pygame.font.init()
W, H = 1100, 950

screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)
clock = pygame.time.Clock()

green_stars = 5
red_stars = 5

soldiers = []
players = []
blocks = []
cities = []
cc = []

main_font = pygame.font.SysFont("comicsans", 50)

red_stars_surface = main_font.render(f"Red Player Stars: {red_stars}", 1, (255, 255, 255))
green_stars_surface = main_font.render(f"Green Player Stars: {green_stars}", 1, (255, 255, 255))

next_turn = NextTurn()
actual_bg = pygame.transform.scale(pygame.image.load("assets/actual_bg.png"), (W, H)).convert()
green_block_image = pygame.transform.scale(pygame.image.load("assets/green-block.png"), (50, 50)).convert()
red_block_image = pygame.transform.scale(pygame.image.load("assets/red-block.png"), (50, 50)).convert()
house_image = pygame.transform.scale(pygame.image.load("assets/house.png"), (50, 50)).convert_alpha()
cursor_image = pygame.transform.scale(pygame.image.load("assets/cursor.png"), (40, 40)).convert_alpha()
red_house_image = pygame.transform.scale(pygame.image.load("assets/red-house.png"), (50, 50)).convert_alpha()
green_house_image = pygame.transform.scale(pygame.image.load("assets/green-house.png"), (50, 50)).convert_alpha()

cursor = Cursor(cursor_image, (0, 0))

def end():
  pass

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

def choose_color_city(img):
  ret = random.choice(cities)
  cities.remove(ret)
  ret.image = img
  return ret

red_cities = [choose_color_city(red_house_image)]
green_cities = [choose_color_city(green_house_image)]

def collision(obj1, obj2):
  offset_x = obj2.x - obj1.coord[0]
  offset_y = obj2.y - obj1.coord[1]

  if obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None:
    return True
  else:
    return False

# throw local var assingment error shit do not use
def show_options(turn, city_clr):
  if city_clr == "none":
    pass
  elif turn == "green" and city_clr == "red":
    pass
  elif turn == "red" and city_clr == "red":
    pass
  elif turn == "green" and city_clr == "green":
    pass
  elif turn == "red" and city_clr == "green":
    pass

def redraw():
  screen.blit(actual_bg, (0, 0))

  for block in blocks:
    block.draw(screen)
  for city in cities:
    city.draw(screen)
  for c in red_cities:
    c.draw(screen)
  for c in green_cities:
    c.draw(screen)
  for soldier in soldiers:
    soldier.draw(screen)

  screen.blit(turn_label, (10, 880))
  screen.blit(next_turn.image, next_turn.coord)
  cursor.draw(screen)

def update():
  global turn_label
  turn_label = main_font.render(f"Turn: {turn}", 1, (255, 255, 255))

  for soldier in soldiers:
    if soldier.health <= 0:
      soldiers.remove(soldier)

  for i in cities:
    if i.selected:
      i.image = pygame.transform.scale(pygame.image.load("assets/house-selected.png"), (50, 50)).convert_alpha()
      i.mask = pygame.mask.from_surface(i.image)
      show_options(turn, "none")
    else:
      i.image = pygame.transform.scale(pygame.image.load("assets/house.png"), (50, 50)).convert_alpha()
      i.mask = pygame.mask.from_surface(i.image)

  for i in green_cities:
    if i.selected:
      i.image = pygame.transform.scale(pygame.image.load("assets/green-house-selected.png"), (50, 50)).convert_alpha()
      i.mask = pygame.mask.from_surface(i.image)
      show_options(turn, "green")
    else:
      i.image = pygame.transform.scale(pygame.image.load("assets/green-house.png"), (50, 50)).convert_alpha()
      i.mask = pygame.mask.from_surface(i.image)

  for i in red_cities:
    if i.selected:
      i.image = pygame.transform.scale(pygame.image.load("assets/red-house-selected.png"), (50, 50)).convert_alpha()
      i.mask = pygame.mask.from_surface(i.image)
      show_options(turn, "red")
    else:
      i.image = pygame.transform.scale(pygame.image.load("assets/red-house.png"), (50, 50)).convert_alpha()
      i.mask = pygame.mask.from_surface(i.image)

  if len(cities) <= 0:
    end()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()
    elif event.type == pygame.MOUSEMOTION:
      cursor.coord = event.pos
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if collision(cursor, next_turn):
        if turn == "green":
          turn = "red"
        else: 
          turn = "green"

        for i in range(len(green_cities) - 1):
          green_stars += 1
        for i in range(len(red_cities) - 1):
          red_stars += 1

      # clearing selected cities
      for i in cities:
        if i.selected:
          i.selected = False
      for i in red_cities:
        if i.selected:
          i.selected = False
      for i in green_cities:
        if i.selected:
          i.selected = False

      # selecting cities
      for i in cities:
        if collision(cursor, i):
          i.selected = True
      for i in green_cities:
        if collision(cursor, i):
          i.selected = True
      for i in red_cities:
        if collision(cursor, i):
          i.selected = True

  update()
  redraw()

  pygame.display.update()
  clock.tick(60)
