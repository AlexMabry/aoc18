def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def prange(lst, x_y):
    return min(lst, key=lambda p: p[x_y])[x_y], max(lst, key=lambda p: p[x_y])[x_y], 1


pts = list(map(lambda line: tuple([int(n) for n in line.split(", ")]), open('input.txt').readlines()))
aggs = [sum([manhattan(p1, (x, y)) for p1 in pts]) for x in range(*prange(pts, 0)) for y in range(*prange(pts, 1))]
print(len(list(filter(lambda sum: sum < 10000, aggs))))
