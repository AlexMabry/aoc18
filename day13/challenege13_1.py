from enum import Enum


class Direction(Enum):
    UP = '^'
    RIGHT = '>'
    DOWN = 'v'
    LEFT = '<'
    CRASHED = 'X'


class NextDecision(Enum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2


class Cart:
    left = {Direction.UP: Direction.LEFT,
            Direction.LEFT: Direction.DOWN,
            Direction.DOWN: Direction.RIGHT,
            Direction.RIGHT: Direction.UP}

    right = {Direction.UP: Direction.RIGHT,
             Direction.RIGHT: Direction.DOWN,
             Direction.DOWN: Direction.LEFT,
             Direction.LEFT: Direction.UP}

    next = {NextDecision.STRAIGHT: NextDecision.RIGHT,
            NextDecision.LEFT: NextDecision.STRAIGHT,
            NextDecision.RIGHT: NextDecision.LEFT}

    def __init__(self, x: int, y: int, char: str):
        self.x = x
        self.y = y
        self.direction = Direction(char)
        self.decision = NextDecision.LEFT

    def __repr__(self):
        return f'({self.x: <3},{self.y: <3}) {self.direction.value} {self.decision}'

    def __lt__(self, other):
        return (self.y, self.x) <= (other.y, other.x)

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __hash__(self):
        return hash((self.x, self.y))

    def turn_left(self):
        self.direction = Cart.left[self.direction]

    def turn_right(self):
        self.direction = Cart.right[self.direction]

    def reach_intersection(self):
        if self.decision == NextDecision.LEFT:
            self.turn_left()
        elif self.decision == NextDecision.RIGHT:
            self.turn_right()

        self.decision = Cart.next[self.decision]

    def move_forward(self):
        self.y += -1 if self.direction == Direction.UP else 1 if c.direction == Direction.DOWN else 0
        self.x += -1 if self.direction == Direction.LEFT else 1 if c.direction == Direction.RIGHT else 0


tracks = [[char for char in row] for row in open('input.txt', 'r').readlines()]
carts = []
for iy, row in enumerate(tracks):
    for ix, c in enumerate(row):
        if c == '<' or c == '>':
            carts.append(Cart(ix, iy, c))
            tracks[iy][ix] = '-'
        elif c == 'v' or c == '^':
            carts.append(Cart(ix, iy, c))
            tracks[iy][ix] = '|'

while carts:
    for c in sorted(carts):
        c.move_forward()
        if tracks[c.y][c.x] == '\\':
            if c.direction == Direction.UP or c.direction == Direction.DOWN:
                c.turn_left()
            else:
                c.turn_right()
        elif tracks[c.y][c.x] == '/':
            if c.direction == Direction.UP or c.direction == Direction.DOWN:
                c.turn_right()
            else:
                c.turn_left()
        elif tracks[c.y][c.x] == '+':
            c.reach_intersection()

        crashed_carts = list(filter(lambda match: match == c, carts))
        if len(crashed_carts) == 2:
            print(c)
            exit()
