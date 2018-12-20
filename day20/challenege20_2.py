from collections import deque, namedtuple, defaultdict

Point = namedtuple('Point', ['x', 'y'])

parent = deque()
current = {'kids': [], 'loc': Point(0, 0), 'dist': 0}
all_rooms = defaultdict(lambda: 100000)

for char in open('input.txt', 'r').readline():
    if char in 'NSEW':
        current['dist'] += 1
        current['loc'] = Point(current['loc'].x + (1 if char == 'E' else -1 if char == 'W' else 0),
                               current['loc'].y + (1 if char == 'N' else -1 if char == 'S' else 0))
        all_rooms[current['loc']] = min([current['dist'], all_rooms[current['loc']]])

    if char in '^(':
        parent.append(current)

    if char in '(|':
        current = {'kids': [], 'loc': parent[-1]['loc'], 'dist':  parent[-1]['dist']}
        parent[-1]['kids'].append(current)

    if char in ')$':
        current = parent.pop()

print(len([room for room in all_rooms.values() if room > 1000]))
