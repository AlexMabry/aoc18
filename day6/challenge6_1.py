def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def read_point(line):
    return tuple([int(n) for n in line.split(", ")])


def prange(points, x_y, extra=0):
    return min(points, key=lambda p: p[x_y])[x_y] - extra, max(points, key=lambda p: p[x_y])[x_y] + extra, 1


def closest(point_list, p2):
    results = sorted({p1: manhattan(p1, p2) for p1 in point_list}.items(), key=lambda p: p[1])
    return results[0][0] if results[0][1] != results[1][1] else (0, 0)


def group_size(points, extra):
    dist = [closest(points, (x, y)) for x in range(*prange(points, 0, extra)) for y in range(*prange(points, 1, extra))]
    return set({point: dist.count(point) for point in points}.items())


coords = list(map(read_point, open('input.txt').readlines()))
print(max(group_size(coords, 0).intersection(group_size(coords, 10)), key=lambda p: p[1])[1])
