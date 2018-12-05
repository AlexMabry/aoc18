import string

f = open('input.txt', 'r')
polymer = f.readline()


def react(poly):
    unit = 0
    while unit <= len(poly) - 2:
        if abs(ord(poly[unit]) - ord(poly[unit + 1])) == 32:
            poly = poly[:unit] + poly[unit+2:]
            unit = unit if unit == 0 else unit-1
        else:
            unit += 1
    return poly


results = {c: len(react(polymer.replace(c, '').replace(c.upper(), ''))) for c in string.ascii_lowercase}
print(min(results.items(), key=lambda item: item[1]))
