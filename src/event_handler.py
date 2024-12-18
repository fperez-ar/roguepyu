from typing import Callable 
# event handlers
_events: dict = {}

def add_event(key: str, fn: Callable[..., None]):
  if key in _events:
    return False
  _events[key] = fn
  return True

def remove_event(key: str):
  del _events[key]
  
def dispatch(key: str, **kwargs):
  if key in _events:
    print('\tev:', key)
    _events[key](**kwargs)