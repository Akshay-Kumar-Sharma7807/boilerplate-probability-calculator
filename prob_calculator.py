import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **colors):
    self.hat = colors
    self.contents = []
    for color in colors:
      for i in range(colors[color]):
        self.contents.append(color)

  def draw(self, n):
    contents = copy.copy(self.contents)
    if n >= len(self.contents):
      return self.contents
    draw = []
    for i in range(n):
      draw.append(contents.pop(random.randrange(len(contents))))


    self.contents = contents
    return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  for experiment in range(num_experiments):
    copyhat = copy.copy(hat)
    draw = copyhat.draw(num_balls_drawn)
    found = True
    for expected_ball in expected_balls:
      if expected_balls[expected_ball] > draw.count(expected_ball):
        found = False
    if found:
      m += 1
  
  probability = m / num_experiments
  return probability
        
