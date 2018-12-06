def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def prange(lst, x_y, extra=0):
    return min(lst, key=lambda p: p[x_y])[x_y] - extra, max(lst, key=lambda p: p[x_y])[x_y] + extra, 1


def closest(lst, p2):
    results = sorted({p1: manhattan(p1, p2) for p1 in lst}.items(), key=lambda p: p[1])
    return results[0][0] if results[0][1] != results[1][1] else (0, 0)


def group_size(lst, extra=0):
    dist = [closest(lst, (x, y)) for x in range(*prange(lst, 0, extra)) for y in range(*prange(lst, 1, extra))]
    return set({point: dist.count(point) for point in lst}.items())


coords = list(map(lambda line: tuple([int(n) for n in line.split(", ")]), open('input.txt').readlines()))
print(max(group_size(coords).intersection(group_size(coords, 10)), key=lambda p: p[1])[1])
