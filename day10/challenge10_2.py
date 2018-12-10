import re
from collections import namedtuple

Star = namedtuple('Star', ['loc', 'rate'])
Point = namedtuple('Point', ['x', 'y'])

p = re.compile('.*<([-\s][0-9]+), ([-\s][0-9]+)> .*<([-\s][0-9]+), ([-\s][0-9]+)>')
lines = map(lambda l: p.match(l).groups(), open('input.txt', 'r').readlines())
stars = map(lambda g: Star(Point(int(g[0]), int(g[1])), Point(int(g[2]), int(g[3]))), lines)

height = 21
seconds = 0
while height > 10:
    stars = [Star(Point(star.loc.x + star.rate.x, star.loc.y + star.rate.y), star.rate) for star in stars]
    height = max(stars, key=lambda s: s.loc.y).loc.y - min(stars, key=lambda s: s.loc.y).loc.y
    seconds += 1

canvas = [['.' for _ in range(64)] for _ in range(12)]
y_min = min(stars, key=lambda s: s.loc.y).loc.y - 1
x_min = min(stars, key=lambda s: s.loc.x).loc.x - 1

for dot in stars:
    canvas[dot.loc.y - y_min][dot.loc.x - x_min] = '*'

for row in canvas:
    print(''.join(row))

print(seconds)
