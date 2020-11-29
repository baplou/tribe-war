#!/usr/bin/env python3
import lib
import pygame

W, H = 1080, 850
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Tribe War")
clock = pygame.time.Clock()

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      quit()

  pygame.display.update()
  clock.tick(60)
