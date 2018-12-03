import re
from collections import defaultdict

f = open('input.txt', 'r')
lines = f.readlines()


def process_lines(line):
    m = re.match('#(?P<cl>[0-9]+) @ (?P<x1>[0-9]+),(?P<y1>[0-9]+): (?P<x2>[0-9]+)x(?P<y2>[0-9]+)', line)
    g = {n: int(v) for (n, v) in m.groupdict().items()}
    return g['cl'], [(x, y) for x in range(g['x1'], g['x1'] + g['x2'], 1) for y in range(g['y1'], g['y1'] + g['y2'], 1)]


claims = dict(map(process_lines, lines))
counts = defaultdict(int)
for xy in [xy for xys in claims.values() for xy in xys]:
    counts[xy] += 1

overloaded = list(filter(lambda num: num > 1, counts.values()))
print(len(overloaded))
