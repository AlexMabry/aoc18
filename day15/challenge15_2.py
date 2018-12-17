from enum import Enum


class Puzzle:
    def __init__(self, cave, elf_power):
        self.round = 0
        self.size = 32
        self.locations = {point: Location(point) for point in cave.keys()}
        self.units = [Unit(self.locations[point], char, 3 if char == 'G' else elf_power) for point, char in cave.items() if char == 'G' or char == 'E']
        for (x, y), spot in self.locations.items():
            spot.links.extend([self.locations[loc] for loc in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)] if loc in cave])

    def goblins(self):
        return [unit for unit in self.units if unit.type == UnitType.GOBLIN]

    def elves(self):
        return [unit for unit in self.units if unit.type == UnitType.ELF]

    def play_game(self):
        while self.goblins() and self.elves():
            order = list(sorted(self.units))
            for unit in order:
                enemies = self.elves() if unit.type == UnitType.GOBLIN else self.goblins()
                target = unit.find_target(enemies)
                if target and target.attacked(unit.power):
                    self.units.remove(target)

            if self.elves() and self.goblins():
                self.round += 1

        return sum([unit.hp for unit in self.units]) * self.round


class Location:
    def __init__(self, loc):
        self.loc: (int, int) = loc
        self.unit: Unit = None
        self.links: [Location] = []

    def __repr__(self):
        return f'{self.unit.type.value if self.unit else "."}'

    def __lt__(self, other):
        return (self.loc[1], self.loc[0]) < (other.loc[1], other.loc[0])

    def possible_moves(self):
        return [link for link in self.links if not link.unit]

    def possible_distances(self):
        current_distance = 0
        steps = self.possible_moves()
        result = {self: current_distance}
        while steps:
            current_distance += 1
            result = {**result, **{neighbor: current_distance for neighbor in steps}}
            steps = set([mv for neighbor in steps for mv in neighbor.possible_moves() if mv not in result])

        return result

    def best_path(self, end):
        distances = end.loc.possible_distances()
        return self.best_path_recur(end.loc, [], distances)

    def best_path_recur(self, end, path, distances):
        if end in self.links:
            path.append(end)
        else:
            options = {mv: distances[mv] for mv in self.possible_moves() if mv in distances and mv not in path}
            if options:
                shortest_distance = min(options.values())
                step = min([mv for mv, dist in options.items() if dist == shortest_distance])
                return step.best_path_recur(end, [*path, step], distances)

        return path

    def occupy(self, unit):
        self.unit = unit

    def vacate(self):
        self.unit = None


class UnitType(Enum):
    GOBLIN = 'G'
    ELF = 'E'


class Unit:
    def __init__(self, loc: Location, unit_type, power):
        self.loc = loc
        self.loc.occupy(self)
        self.type = UnitType(unit_type)
        self.hp = 200
        self.power = power

    def __repr__(self):
        return f'{self.type.value}({self.hp})'

    def __lt__(self, other):
        return self.loc < other.loc

    def is_alive(self):
        return self.hp > 0

    def step_to_closest_enemy(self, enemies):
        enemy_dist = {enemy: self.loc.best_path(enemy) for enemy in enemies}
        enemy_dist = {enemy: path for enemy, path in enemy_dist.items() if path}
        if enemy_dist:
            shortest_path = len(min(enemy_dist.values(), key=lambda v: len(v)))
            close_enemies = [enemy for enemy, path in enemy_dist.items() if len(path) == shortest_path]
            closest_enemy = min(close_enemies)
            return enemy_dist[closest_enemy][0]
        else:
            return None

    def move_to_closest_enemy(self, enemies):
        step = self.step_to_closest_enemy(enemies)
        if step:
            self.loc.vacate()
            self.loc = step
            step.occupy(self)

    def target_in_range(self):
        units_in_range = [nb.unit for nb in self.loc.links if nb.unit and nb.unit.type != self.type]
        if units_in_range:
            lowest_hp = min(units_in_range, key=lambda u: u.hp).hp
            return sorted([enemy for enemy in units_in_range if enemy.hp == lowest_hp])[0]
        else:
            return None

    def find_target(self, enemies):
        target = None
        if self.is_alive():
            target = self.target_in_range()
            if not target:
                self.move_to_closest_enemy(enemies)
                target = self.target_in_range()

        return target

    def attacked(self, damage):
        if self.is_alive():
            self.hp -= damage
            if self.hp <= 0:
                self.loc.vacate()
                return True

        return False


lines = open('input.txt', 'r').readlines()
cavern = {(ix, iy): char for iy, row in enumerate(lines) for ix, char in enumerate(row.strip()) if char != '#'}

for elf_pow in range(25, 400):
    print('Trying:', elf_pow)
    puzzle = Puzzle(cavern, elf_pow)
    answer = puzzle.play_game()
    print('Elves left:', len(puzzle.elves()))
    if len(puzzle.elves()) == 10:
        print('ANSWER', answer)
        exit()
