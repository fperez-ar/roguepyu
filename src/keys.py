from pygame import *
from pygame import quit as gamequit
from event_handler import dispatch
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

def get_dir(key_down_event) -> tuple[int,int] | None:
  dx, dy = 0, 0
  if key_down_event in [K_LEFT, K_a]:
    dx = -1
  if key_down_event in [K_RIGHT, K_d]:
    dx = 1
  if key_down_event in [K_UP, K_w]:
    dy = -1
  if key_down_event in [K_DOWN, K_s]:
    dy = 1
  if dx == 0 and dy == 0:
    return None
  return dx, dy