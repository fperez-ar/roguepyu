#!/usr/bin/env python
import pygame
from grid import Grid
from time import sleep
from player import Player
from keys import get_dir
from event_handler import add_event
# settings  _events[key] = fn

pygame.init()
pygame.display.set_caption('game loop')
fps = 60
height = 720
width = 1280
bg_color = (255, 255, 255)
# game entitites
entities = []

def update(entities, **kwargs):
  for e in entities:
    e.update(**kwargs)

def redraw(win, entities):
  win.fill(bg_color)
  for e in entities:
    e.draw(win)
    grid.draw(win)
    pygame.display.update()


def move(grid, entity, new_pos: tuple[int,int]):
  x,y = new_pos
  grid_space = grid.get(x, y)
  if grid_space == 0:
    grid.set(x,y, entity)
  
def game_loop(entities):
  global game_state
  player = entities[0]
  while game_state:
    for ev in pygame.event.get():
      # print(event)
      if ev.type == pygame.QUIT:
        pygame.quit()
      if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE or ev.key == pygame.K_q:
          game_state = None
        direction = get_dir(ev)
        x,y = player.get_pos()
        if direction == 'up':
          y = player.y - 1
        if direction == 'down':
          y = player.y + 1
        if direction == 'left':
          x = player.x - 1
        if direction == 'right':
          x = player.x + 1
        # try to set new pos
        grid.set((x,y), player)
    
    dt = clock.tick(fps) / 1000
    update(entities, grid=grid)
    redraw(win, entities)
    clock.tick(fps)
  pygame.quit()

game_state = True
clock = pygame.time.Clock()
win = pygame.display.set_mode((width, height))

# entities
size = 50
grid = Grid(height, width, size)
entities.append(Player(0,0,size,size,(0,255,255)))
game_loop(entities)