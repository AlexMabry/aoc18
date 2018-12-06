def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def read_point(line):
    return tuple([int(n) for n in line.split(", ")])


def prange(points, x_y, extra=0):
    return min(points, key=lambda p: p[x_y])[x_y] - extra, max(points, key=lambda p: p[x_y])[x_y] + extra, 1


def agg(point_list, p2):
    return sum([manhattan(p1, p2) for p1 in point_list])


def group_size(points, extra=0):
    aggs = [agg(points, (x, y)) for x in range(*prange(points, 0, extra)) for y in range(*prange(points, 1, extra))]
    return list(filter(lambda sum: sum < 10000, aggs))


coords = list(map(read_point, open('input.txt').readlines()))
print(len(group_size(coords)))
