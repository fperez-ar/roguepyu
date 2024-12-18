from pygame import *
from pygame import quit as gamequit
from event_handler import dispatch
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def get_dir(ev):
  # print(ev.key)
  if ev.key == K_LEFT or ev.key == K_a:
    # dispatch('left')
    return LEFT
  if ev.key == K_RIGHT or ev.key == K_d:
    # dispatch('right')
    return RIGHT
  if ev.key == K_UP or ev.key == K_w:
    # dispatch('up')
    return UP
  if ev.key == K_DOWN or ev.key == K_s:
    # dispatch('down')
    return DOWN
  if ev.key == K_ESCAPE or ev.key == K_q:
    dispatch('quit')
