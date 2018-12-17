from collections import namedtuple
from time import time

SERIAL_NUM = 9424
Point = namedtuple('Point', ['x', 'y'])

start = time()
points = [Point(x, y) for x in range(1, 301) for y in range(1, 301)]
scores = {point: ((((point.x+10)*point.y + SERIAL_NUM)*(point.x+10) % 1000) // 100) - 5 for point in points}
square_org = [(p, s) for p in points for s in range(4, 20) if p.x+s < 301 and p.y+s < 301]
squares = [[Point(xp, yp) for xp in range(p.x, p.x+s) for yp in range(p.y, p.y+s)] for p, s in square_org]
square_scores = {(s[0], len(s)): sum(scores.get(p, -100) for p in s) for s in squares}

print(max(square_scores.items(), key=lambda score: score[1]))
print(time() - start)
