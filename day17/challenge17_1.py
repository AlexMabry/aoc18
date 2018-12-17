import re
from collections import namedtuple, deque

Point = namedtuple('Point', ['x', 'y'])


def get_clay(lines):
    blocks = set()
    for line in lines:
        groups = re.match('[xy]=([0-9]+), [xy]=([0-9]+)..([0-9]+)', line).groups()
        if line.startswith('x'):
            blocks |= set([Point(int(groups[0]), y) for y in range(int(groups[1]), int(groups[2])+1)])
        else:
            blocks |= set([Point(x, int(groups[0])) for x in range(int(groups[1]), int(groups[2])+1)])
    return blocks


def connected_water(drop, connected):
    wet = [n for n in [Point(drop.x - 1, drop.y), Point(drop.x + 1, drop.y)] if n in all_h2o or n in falling]
    for neighbor in [drip for drip in wet if drip not in connected]:
        connected.add(neighbor)
        connected_water(neighbor, connected)
    return connected


clay = get_clay(open('input.txt', 'r').readlines())
min_x, max_x = min([x for (x, _) in clay]), max([x for (x, _) in clay])
min_y, max_y = min([y for (_, y) in clay]), max([y for (_, y) in clay])

all_h2o = {Point(500, min_y)}
new_h2o = deque([Point(500, min_y)])
falling = {Point(500, min_y)}

while new_h2o:
    point = new_h2o[-1]
    below = Point(point.x, point.y + 1)
    if below.y > max_y:
        falling |= set([d for d in new_h2o if Point(d.x, d.y - 1) in new_h2o or Point(d.x, d.y + 1) in new_h2o])
        new_h2o = [d for d in new_h2o if d not in falling]
    else:
        if below in all_h2o and [drip for drip in connected_water(below, set()) if drip in falling]:
            falling |= set([d for d in new_h2o if Point(d.x, d.y - 1) in new_h2o or Point(d.x, d.y + 1) in new_h2o])
            new_h2o = [d for d in new_h2o if d not in falling]
        elif below not in clay and below not in all_h2o:
            all_h2o.add(below)
            new_h2o.append(below)
        else:
            next_drop = new_h2o.pop()
            if next_drop.y < max_y:
                sides = [Point(next_drop.x - 1, next_drop.y), Point(next_drop.x + 1, next_drop.y)]
                new_drops = [side for side in sides if side not in clay and side not in all_h2o]
                new_h2o.extend(new_drops)
                all_h2o |= set(new_drops)

top_water = set()
for droplet in falling:
    connected_water(droplet, top_water)

still = all_h2o.difference(top_water).difference(falling)

for y in range(min_y, max_y+1):
    print(''.join(['#' if (x, y) in clay else '~' if (x, y) in still else '|' if (x, y) in all_h2o else ' ' for x in range(min_x, max_x + 1)]))

print(len(all_h2o))
