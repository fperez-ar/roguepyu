#!/usr/bin/env python
import pygame
from grid import Grid
from time import sleep
from player import Player
from entity import Entity
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


def move(grid, player: Entity, direction : tuple[int,int]):
# get current position
  cx,cy = player.get_pos()
  # get new direction
  dx, dy = direction
  # calculate new postion
  nx = cx + dx
  ny = cy + dy
  # try to set new pos
  grid.set((nx,ny), player)
    
def game_loop(entities):
  global game_state
  player = entities[0]
  while game_state:
    # dt = clock.tick(fps) / 1000
    update(entities, grid=grid)
    redraw(win, entities)
    clock.tick(fps)
    for ev in pygame.event.get():
      # print(event)
      if ev.type == pygame.QUIT:
        pygame.quit()
      if ev.type == pygame.KEYDOWN:
        if ev.key == pygame.K_ESCAPE or ev.key == pygame.K_q:
          game_state = None
        direction = get_dir(ev.key)
        if direction:
          move(grid, player, direction)
        
  pygame.quit()

game_state = True
clock = pygame.time.Clock()
win = pygame.display.set_mode((width, height))
# entities
size = 50
grid = Grid(height, width, size)
entities.append(Player(0,0,size,(0,255,255)))
entities.append(Entity(0,2,size,(0,255,10)))
entities[1].name = 'pepe'
# grid
for e in entities:
  grid.set(e.get_pos(), e)
game_loop(entities)