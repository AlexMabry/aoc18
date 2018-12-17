import re
from collections import namedtuple, deque

# guessed = 121435(H), 39558(H)

Point = namedtuple('Point', ['x', 'y'])

lines = open('input.txt', 'r').readlines()
clay = set()
for line in lines:
    groups = re.match('[xy]=([0-9]+), [xy]=([0-9]+)..([0-9]+)', line).groups()
    if line.startswith('x'):
        clay |= set([Point(int(groups[0]), y) for y in range(int(groups[1]), int(groups[2])+1)])
    else:
        clay |= set([Point(x, int(groups[0])) for x in range(int(groups[1]), int(groups[2])+1)])


min_x = min([x for (x, y) in clay])
max_x = max([x for (x, y) in clay])
min_y = min([y for (x, y) in clay])
max_y = max([y for (x, y) in clay])

old_water = set([Point(500, min_y)])


def print_ground():
    for y in range(min_y-1, max_y+2):
        print(''.join(['#' if (x, y) in clay else '|' if (x, y) in falling_water else '~' if (x, y) in old_water else ' ' for x in range(min_x-2, max_x+2)]))
    print()


def sideways(drop):
    if drop.y + 1 < max_y + 1:
        sides = [Point(drop.x - 1, drop.y), Point(drop.x + 1, drop.y)]
        return [side for side in sides if side not in clay and side not in old_water]
    else:
        return []


def connected_water(drop, answer):
    wet = [n for n in [Point(drop.x - 1, drop.y), Point(drop.x + 1, drop.y)] if n in old_water or n in falling_water]
    for neighbor in [drip for drip in wet if drip not in answer]:
        answer.append(neighbor)
        connected_water(neighbor, answer)


def already_falling(drop):
    wet_neighbors = []
    connected_water(drop, wet_neighbors)
    return [drip for drip in wet_neighbors if drip in falling_water]


def remove_falling():
    global falling_water, new_water
    falling_water |= set([drop for drop in new_water if
                          Point(drop.x, drop.y - 1) in new_water or Point(drop.x, drop.y + 1) in new_water])
    new_water = [drop for drop in new_water if drop not in falling_water]


new_water = deque([Point(500, min_y)])
falling_water = {Point(500, min_y)}

while new_water:
    point = new_water[-1]
    below = Point(point.x, point.y + 1)
    if below.y >= max_y+1:
        remove_falling()
    else:
        if below not in clay and below not in old_water:
            old_water.add(below)
            new_water.append(below)

            below_below = Point(below.x, below.y + 1)
            if below_below in old_water and already_falling(below_below):
                remove_falling()
        else:
            new_drops = sideways(new_water.pop())
            new_water.extend(new_drops)
            old_water |= set(new_drops)

print_ground()

print(len(old_water))