from collections import namedtuple, defaultdict
from enum import Enum

Point = namedtuple('Point', ['x', 'y'])

# G = 194756(L), 507755


class Area(Enum):
    NONE = ' '
    OPEN = '.'
    TREE = '|'
    YARD = '#'


def around_me(pt):
    surroundings = [forest.get(point, Area.NONE) for point in neighbors[pt]]
    return {area.name: surroundings.count(area) for area in set(surroundings) if area != Area.NONE}


def nothing():
    return Area.NONE


def next_forest(matrix):
    new_forest = defaultdict(nothing)
    surroundings = {point: around_me(point) for point in list(matrix.keys())}
    for point, area in matrix.items():
        if area == Area.OPEN and surroundings[point].get('TREE', 0) >= 3:
            new_forest[point] = Area.TREE
        elif area == Area.TREE and surroundings[point].get('YARD', 0) >= 3:
            new_forest[point] = Area.YARD
        elif area == Area.YARD and (surroundings[point].get('YARD', 0) < 1 or surroundings[point].get('TREE', 0) < 1):
            new_forest[point] = Area.OPEN
        else:
            new_forest[point] = area
    return new_forest


def print_forest(matrix):
    for y in range(50):
        print(''.join([area.value for area in [matrix[Point(x, y)] for x in range(50)]]))


lines = open('input.txt', 'r').readlines()
forest = defaultdict(nothing)

for iy, line in enumerate(lines):
    for ix, char in enumerate(line.strip()):
        forest[Point(ix, iy)] = Area(char)


neighbors = {pt: [Point(x, y) for x in range(pt.x-1, pt.x+2) for y in range(pt.y-1, pt.y+2) if Point(x, y) != pt] for pt in forest.keys()}

for times in range(10):
    forest = next_forest(forest)
    print_forest(forest)
    print()
    print()
    print()


        # contents = list(forest.values())
        # trees = contents.count(Area.TREE)
        # yards = contents.count(Area.YARD)
        # print(times, round, trees*yards)
