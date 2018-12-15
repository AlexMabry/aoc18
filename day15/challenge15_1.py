from enum import Enum


class Contains(Enum):
    WALL = '#'
    OPEN = '.'
    GOBLIN = 'G'
    ELF = 'E'


class Map:
    def __init__(self, lines):
        self.locations = [Location(ix, iy, char) for iy, row in enumerate(lines) for ix, char in enumerate(row.strip())]
        self.goblins = [Unit(loc) for loc in filter(lambda l: l.occ == Contains.GOBLIN, self.locations)]
        self.elves = [Unit(loc) for loc in filter(lambda l: l.occ == Contains.ELF, self.locations)]

    def __repr__(self):
        return f'GOBLINS: {len(self.goblins)}\n' \
               f'ELVES: {len(self.elves)}'


class Location:
    def __init__(self, x, y, occ):
        self.loc = (x, y)
        self.occ = Contains(occ)
        self.up = (x, y-1) if y > 0 else None
        self.down = (x, y+1) if y < 31 else None
        self.left = (x-1, y) if x > 0 else None
        self.right = (x+1, y) if x < 31 else None

    def __repr__(self):
        return f'{self.loc} - {self.occ.name}'


class Unit:
    def __init__(self, loc):
        self.loc = loc
        self.hp = 200

    def __repr__(self):
        return f'{self.loc}'


puzzle = Map(open('input.txt', 'r').readlines())
print(puzzle)
