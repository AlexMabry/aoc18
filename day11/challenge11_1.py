from collections import namedtuple

SERIAL_NUM = 9424
Point = namedtuple('Point', ['x', 'y'])

points = [Point(x, y) for x in range(1, 301) for y in range(1, 301)]
scores = {point: ((((point.x+10)*point.y + SERIAL_NUM)*(point.x+10) % 1000) // 100) - 5 for point in points}
squares = [[Point(xp, yp) for xp in range(p.x, p.x+3) for yp in range(p.y, p.y+3)] for p in points]
square_scores = {s[0]: sum(scores.get(p, -100) for p in s) for s in squares}

print(max(square_scores.items(), key=lambda score: score[1]))
